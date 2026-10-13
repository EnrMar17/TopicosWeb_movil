import pandas as pd

from entrenar_arbol import NUMERICAS, OBJETIVO
from usar_modelo import es_posible

pd.set_option("display.width", 200)

datos = pd.read_csv("envios_medios.csv")

print("Dominio por clima (% por fila)")
tabla_clima = pd.crosstab(
    datos["clima"], datos[OBJETIVO], normalize="index"
)
print((tabla_clima * 100).round(1))

print("\nDominio por zona (% por fila)")
tabla_zona = pd.crosstab(
    datos["zona_destino"], datos[OBJETIVO], normalize="index"
)
print((tabla_zona * 100).round(1))

print("\nDistancia por medio (mínimo, mediana y máximo)")
resumen_distancia = datos.groupby(OBJETIVO)["distancia_km"].agg(
    ["min", "median", "max"]
)
print(resumen_distancia)

print("\nEtiquetas que rompen las reglas")
datos["etiqueta_posible"] = datos.apply(
    lambda fila: es_posible(fila[OBJETIVO], fila), axis=1
)
etiquetas_imposibles = datos[~datos["etiqueta_posible"]]
print(f"Total: {len(etiquetas_imposibles)}")
if not etiquetas_imposibles.empty:
    print(etiquetas_imposibles[["id_envio", OBJETIVO]])
