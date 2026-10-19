import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.base import clone

NUMERICAS = [
    "distancia_km", "peso_kg", "largo_cm", "ancho_cm",
    "alto_cm", "volumen_l", "fragil", "refrigerado",
    "valor_declarado_mxn", "hora_salida"
]
CATEGORICAS = ["prioridad", "zona_destino", "clima", "trafico"]
OBJETIVO = "medio_recomendado"

datos = pd.read_csv("envios_medios.csv")
x = datos[NUMERICAS + CATEGORICAS]
y = datos[OBJETIVO]

x_entreno, x_prueba, y_entreno, y_prueba = train_test_split(
    x, y, test_size=0.2, stratify=y, random_state=42
)

modelo = joblib.load("modelo_medios.joblib")
exactitud_base = modelo.score(x_prueba, y_prueba) * 100

# 1. Importancia de las 14 columnas originales
nombres = modelo.named_steps["preparacion"].get_feature_names_out()
importancias = pd.Series(
    modelo.named_steps["arbol"].feature_importances_,
    index=nombres
)

def columna_original(nombre):
    nombre = nombre.split("__")[-1]
    for columna in sorted(x.columns, key=len, reverse=True):
        if nombre == columna or nombre.startswith(columna + "_"):
            return columna
    return nombre

importancia = importancias.groupby(
    [columna_original(n) for n in importancias.index]
).sum().reindex(x.columns, fill_value=0).sort_values(ascending=False)

print(" IMPORTANCIA DE LAS COLUMNAS")
print(importancia.round(4).to_string())
print(f"\nExactitud original: {exactitud_base:.2f}%")

# 2. Entrenar un árbol sin cada columna
resultados = []

for columna in x.columns:
    modelo_sin = clone(modelo)
    preparacion = modelo_sin.named_steps["preparacion"]

    preparacion.transformers = [
        (
            nombre,
            transformador,
            [c for c in columnas if c != columna]
            if isinstance(columnas, (list, tuple)) else columnas
        )
        for nombre, transformador, columnas in preparacion.transformers
    ]

    modelo_sin.fit(x_entreno.drop(columns=[columna]), y_entreno)
    exactitud = modelo_sin.score(
        x_prueba.drop(columns=[columna]), y_prueba
    ) * 100

    resultados.append((columna, exactitud, exactitud - exactitud_base))

tabla = pd.DataFrame(
    resultados,
    columns=["Columna eliminada", "Exactitud (%)", "Cambio (puntos porcentuales)"]
).sort_values("Cambio (puntos porcentuales)")

print("\n EFECTO DE ELIMINAR CADA COLUMNA")
print(tabla.round(2).to_string(index=False))

print("\nColumnas que no cambiaron la exactitud:")
print([
    columna for columna, exactitud, cambio in resultados
    if abs(cambio) < 0.0000001
])