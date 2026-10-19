import pandas as pd

datos = pd.read_csv("envios_medios.csv")

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 200)

print("Medios recomendados por hora")
tabla_hora = pd.crosstab(
    datos["hora_salida"],
    datos["medio_recomendado"]
)
print(tabla_hora)

print("\nHoras sin drones")
if "dron" in tabla_hora.columns:
    horas_sin_dron = tabla_hora[
        tabla_hora["dron"] == 0
    ].index.tolist()
else:
    horas_sin_dron = tabla_hora.index.tolist()

print(horas_sin_dron)

datos["horario"] = datos["hora_salida"].apply(
    lambda hora: "noche" if hora < 6 or hora >= 21 else "dia"
)

print("\nCantidad de envios por horario")
print(datos["horario"].value_counts())

print("\nPorcentaje de envios por horario")
print(
    (datos["horario"].value_counts(normalize=True) * 100).round(2)
)

print("\nMedios por horario")
tabla_horario = pd.crosstab(
    datos["horario"],
    datos["medio_recomendado"]
)
print(tabla_horario)

print("\nPorcentaje de medios por horario")
print(
    (pd.crosstab(
        datos["horario"],
        datos["medio_recomendado"],
        normalize="index"
    ) * 100).round(2)
)

print("\nBicicletas y motos a las 20:00 y 21:00")
comparacion = tabla_hora.reindex([20, 21], fill_value=0)
print(comparacion.reindex(
    columns=["bicicleta", "moto"],
    fill_value=0
))

datos["es_de_noche"] = (
    (datos["hora_salida"] < 6) |
    (datos["hora_salida"] >= 21)
).astype(int)

print("\nDistribucion de es_de_noche")
print(datos["es_de_noche"].value_counts())
