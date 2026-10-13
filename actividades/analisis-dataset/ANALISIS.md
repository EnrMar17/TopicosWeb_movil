# Analisis Dataset
# Actividad 1 — El retrato del dataset

## Predicciones

- Deberia dominar la camioneta porque en condiciones de lluvia esta protegeria mas los paquetes.
- La bicicleta o la moto, porque son mas agiles en caso de que haya trafico pesado y consumen menos recursos que una camioneta.
- Considero que entre 5 o 6km porque seria muy tardada la entrega si es mas lejos.
- No deberia haber, para eso estan las reglas que se establecieron.

## Resultados

### Porcentaje de medios según clima 

| Clima | Bicicleta | Camioneta | Dron | Moto |
|---|---:|---:|---:|---:|
| despejado | 32.8 | 16.6 | 13.5 | 37.1 |
| lluvia | 8.5 | 16.7 | 0.0 | 74.8 |
| viento_fuerte | 31.7 | 18.4 | 0.0 | 49.9 |

### Porcentaje de medios según zona 

| Zona | Bicicleta | Camioneta | Dron | Moto |
|---|---:|---:|---:|---:|
| centro | 58.4 | 13.5 | 0.0 | 28.0 |
| periferia | 0.9 | 14.0 | 12.6 | 72.5 |
| residencial | 26.2 | 14.6 | 17.3 | 41.9 |
| rural | 0.0 | 40.8 | 0.0 | 59.2 |

### Distancias por medio (km)

| Medio | Mínimo | Mediana | Máximo |
|---|---:|---:|---:|
| bicicleta | 0.37 | 3.420 | 7.00 |
| camioneta | 0.43 | 8.990 | 59.12 |
| dron | 2.07 | 9.535 | 14.99 |
| moto | 0.34 | 10.630 | 39.90 |

### Etiquetas que rompen las reglas

Total: **0**.

## Comparación con las predicciones

- El medio dominante fue la moto con un 74.8%, en comparacion al 16.7% de la camioneta que predije como el medio dominante. No condisere en este caso que la moto es un medio que usa menos recursos.
- La bicicleta fue el medio dominante con un 58.4%, que propuse como un medio dominante pero lo asegure. No considere el hecho de que en el centro las distancias probablemente no sean muy grandes como para usar una moto.
- La bicicleta tiene un maximo de 7km, falle porque predije entre 5 y 6km.
- Aqui acerte ya que no hubo etiquetas que rompieran las reglas.




