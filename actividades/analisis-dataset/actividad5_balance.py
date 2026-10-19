import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.base import clone
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

datos = pd.read_csv("envios_medios.csv")
modelo_base = joblib.load("modelo_medios.joblib")

from usar_modelo import es_posible

OBJETIVO = "medio_recomendado"
NUMERICAS = [
    "distancia_km", "peso_kg", "largo_cm", "ancho_cm",
    "alto_cm", "volumen_l", "fragil", "refrigerado",
    "valor_declarado_mxn", "hora_salida"
]
CATEGORICAS = ["prioridad", "zona_destino", "clima", "trafico"]

X = datos[NUMERICAS + CATEGORICAS]
y = datos[OBJETIVO]

x_entreno, x_prueba, y_entreno, y_prueba = train_test_split(
    X, y,
    test_size=0.2,
    stratify=y,
    random_state=42
)

resultados = []

def evaluar(x_train, y_train, estrategia, peso=None):
    modelo = clone(modelo_base)

    if peso is not None:
        modelo.set_params(arbol__class_weight=peso)

    modelo.fit(x_train, y_train)
    predicciones = modelo.predict(x_prueba)

    es_dron_real = (y_prueba == "dron")
    es_dron_predicho = (predicciones == "dron")

    precision = precision_score(
        es_dron_real, es_dron_predicho, zero_division=0
    )
    recall = recall_score(
        es_dron_real, es_dron_predicho, zero_division=0
    )

    imposibles = sum(
        not es_posible(medio, x_prueba.iloc[i])
        for i, medio in enumerate(predicciones)
    )

    resultados.append({
        "Estrategia": estrategia,
        "Envíos de entrenamiento": len(x_train),
        "Exactitud (%)": round(accuracy_score(y_prueba, predicciones) * 100, 2),
        "Precision dron (%)": round(precision * 100, 2),
        "Recall dron (%)": round(recall * 100, 2),
        "Veces que predice dron": int(es_dron_predicho.sum()),
        "Sugerencias imposibles": int(imposibles),
        "F1 macro (%)": round(
            f1_score(y_prueba, predicciones, average="macro") * 100, 2
        )
    })

    return modelo

evaluar(x_entreno, y_entreno, "Sin balancear")

entreno = x_entreno.copy()
entreno[OBJETIVO] = y_entreno

cantidad_minima = entreno[OBJETIVO].value_counts().min()

submuestreo = pd.concat([
    grupo.sample(n=cantidad_minima, random_state=42)
    for _, grupo in entreno.groupby(OBJETIVO)
])

x_sub = submuestreo[NUMERICAS + CATEGORICAS]
y_sub = submuestreo[OBJETIVO]

evaluar(x_sub, y_sub, "Submuestreo")

cantidad_maxima = entreno[OBJETIVO].value_counts().max()

sobremuestreo = pd.concat([
    grupo.sample(
        n=cantidad_maxima,
        replace=True,
        random_state=42
    )
    for _, grupo in entreno.groupby(OBJETIVO)
])

x_sobre = sobremuestreo[NUMERICAS + CATEGORICAS]
y_sobre = sobremuestreo[OBJETIVO]

evaluar(x_sobre, y_sobre, "Sobremuestreo")

evaluar(
    x_entreno,
    y_entreno,
    'class_weight="balanced"',
    peso="balanced"
)

tabla = pd.DataFrame(resultados)

print("\nRESULTADOS DE LAS ESTRATEGIAS")
print(tabla.to_string(index=False))

print("\nDrones reales en la prueba:", int((y_prueba == "dron").sum()))

print("\nDETALLE DEL DRON")

for estrategia, modelo in [
    ("Sin balancear", None)
]:
    pass

modelos = [
    ("Sin balancear", x_entreno, y_entreno, None),
    ("Submuestreo", x_sub, y_sub, None),
    ("Sobremuestreo", x_sobre, y_sobre, None),
    ('class_weight="balanced"', x_entreno, y_entreno, "balanced")
]

for nombre, x_train, y_train, peso in modelos:
    modelo = clone(modelo_base)

    if peso is not None:
        modelo.set_params(arbol__class_weight=peso)

    modelo.fit(x_train, y_train)
    pred = modelo.predict(x_prueba)

    reales_dron = y_prueba == "dron"
    pred_dron = pred == "dron"

    detectados = int((reales_dron & pred_dron).sum())
    no_detectados = int((reales_dron & ~pred_dron).sum())
    falsos_dron = int((~reales_dron & pred_dron).sum())

    print(
        f"{nombre}: detectados={detectados}, "
        f"no detectados={no_detectados}, "
        f"predicciones incorrectas de dron={falsos_dron}"
    )

completo = X.copy()
completo[OBJETIVO] = y

maximo_completo = completo[OBJETIVO].value_counts().max()

datos_trampa = pd.concat([
    grupo.sample(
        n=maximo_completo,
        replace=True,
        random_state=42
    )
    for _, grupo in completo.groupby(OBJETIVO)
])

x_trampa = datos_trampa[NUMERICAS + CATEGORICAS]
y_trampa = datos_trampa[OBJETIVO]

x_train_t, x_test_t, y_train_t, y_test_t = train_test_split(
    x_trampa,
    y_trampa,
    test_size=0.2,
    stratify=y_trampa,
    random_state=42
)

modelo_trampa = clone(modelo_base)
modelo_trampa.fit(x_train_t, y_train_t)
pred_trampa = modelo_trampa.predict(x_test_t)

filas_entreno = set(map(tuple, x_train_t.to_numpy()))
filas_repetidas = sum(
    tuple(fila) in filas_entreno
    for fila in x_test_t.to_numpy()
)

reales_dron_t = y_test_t == "dron"
pred_dron_t = pred_trampa == "dron"

imposibles_t = sum(
    not es_posible(medio, x_test_t.iloc[i])
    for i, medio in enumerate(pred_trampa)
)

print("\nTRAMPA DELIBERADA")
print("Filas de entrenamiento:", len(x_train_t))
print("Filas de prueba:", len(x_test_t))
print("Filas de prueba repetidas en entrenamiento:", filas_repetidas)
print("Exactitud (%):", round(accuracy_score(y_test_t, pred_trampa) * 100, 2))
print("Precision dron (%):", round(
    precision_score(reales_dron_t, pred_dron_t, zero_division=0) * 100, 2
))
print("Recall dron (%):", round(
    recall_score(reales_dron_t, pred_dron_t, zero_division=0) * 100, 2
))
print("Veces que predice dron:", int(pred_dron_t.sum()))
print("Sugerencias imposibles:", int(imposibles_t))
