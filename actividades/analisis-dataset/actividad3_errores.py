import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from entrenar_arbol import NUMERICAS, CATEGORICAS, OBJETIVO
from usar_modelo import es_posible

datos = pd.read_csv("envios_medios.csv")

x = datos[NUMERICAS + CATEGORICAS]
y = datos[OBJETIVO]

x_entreno, x_prueba, y_entreno, y_prueba = train_test_split(
    x, y, test_size=0.2, stratify=y, random_state=42
)

modelo = joblib.load("modelo_medios.joblib")
predicciones = modelo.predict(x_prueba)

comparacion = x_prueba.assign(real=y_prueba, predicho=predicciones)
comparacion["id_envio"] = datos.loc[x_prueba.index, "id_envio"]

errores = comparacion[comparacion["real"] != comparacion["predicho"]]
confusiones = errores.groupby(["real", "predicho"]).size().sort_values(ascending=False)

# 1. Resumen de errores
print("Envíos de prueba:", len(x_prueba))
print("Total de errores:", len(errores))
print(f"Porcentaje de errores: {len(errores) / len(x_prueba) * 100:.2f}%")
print("\nTres confusiones más frecuentes:")
print(confusiones.head(3))

# 2. Motos clasificadas como drones
moto_dron = errores[
    (errores["real"] == "moto") & (errores["predicho"] == "dron")
].copy()

noche = (moto_dron["hora_salida"] < 6) | (moto_dron["hora_salida"] >= 21)
moto_dron["dron_posible"] = moto_dron.apply(
    lambda fila: es_posible("dron", fila), axis=1
)

print("\nMoto clasificadas como dron:", len(moto_dron))
print("De noche:", noche.sum())
print("De día:", (~noche).sum())
print("Rechazadas por las reglas:", (~moto_dron["dron_posible"]).sum())
print("Permitidas por las reglas:", moto_dron["dron_posible"].sum())

# 3. Motos clasificadas como bicicletas
moto_bici = errores[
    (errores["real"] == "moto") & (errores["predicho"] == "bicicleta")
]

bicicletas_ok = comparacion[
    (comparacion["real"] == "bicicleta") &
    (comparacion["predicho"] == "bicicleta")
]

print("\nMotos clasificadas como bicicleta:", len(moto_bici))

if not moto_bici.empty:
    print("\nDistancias (km):")
    print(moto_bici["distancia_km"].agg(["min", "mean", "max"]).round(2))

    print("\nComparación de promedios:")
    print(pd.DataFrame({
        "Bicicletas correctas": bicicletas_ok[NUMERICAS].mean(),
        "Motos confundidas": moto_bici[NUMERICAS].mean()
    }).round(2))

    print("\nComparación de categorías (%):")
    for columna in CATEGORICAS:
        tabla = pd.concat([
            bicicletas_ok[columna].value_counts(normalize=True).rename("Bicicletas"),
            moto_bici[columna].value_counts(normalize=True).rename("Motos confundidas")
        ], axis=1).fillna(0).mul(100).round(1)

        print(f"\n{columna}:")
        print(tabla)