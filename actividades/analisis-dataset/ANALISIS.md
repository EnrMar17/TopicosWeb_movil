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

### Limites por medio

| Medio | Peso máximo (kg) | Volumen máximo (l) | Distancia máxima (km) |
|---|---:|---:|---:|
| bicicleta | 8.0 | 40.0 | 7.0 |
| moto | 25.0 | 90.0 | 40.0 |
| camioneta | 1000.0 | 3000.0 | 1000.0 |
| dron | 2.5 | 12.0 | 15.0 |

### Etiquetas que rompen las reglas

Total: **0**.

## Comparación con las predicciones

- El medio dominante fue la moto con un 74.8%, en comparacion al 16.7% de la camioneta que predije como el medio dominante. No condisere en este caso que la moto es un medio que usa menos recursos.
- La bicicleta fue el medio dominante con un 58.4%, que propuse como un medio dominante pero no lo asegure. No considere el hecho de que en el centro las distancias probablemente no sean muy grandes como para usar una moto.
- La bicicleta tiene un maximo de 7km, falle porque predije entre 5 y 6km.
- Aqui acerte ya que no hubo etiquetas que rompieran las reglas.

## Preguntas.

- ¿En qué zonas y con qué climas el dron nunca aparece? ¿Qué regla del paso 12 lo explica en cada caso?
No aparecen en la zonta centro ni en condiciones de luvia. Esta establecido que el dron solo puede entregar en zonas que no sean la centro, el clima debe estar despejado y no puede ser de noche. 
- La bicicleta casi no va a la periferia, aunque ninguna regla se lo prohíbe. ¿Qué otra columna lo explica? Demuéstrenlo con un número.
Debido a que la periferia se encuentra en el limite de los 7km que tiene la bicicleta, es por eso que hay tan pocas bicicletas en esa zona.
- Comparen los máximos de distancia, peso y volumen de cada medio con la tabla LIMITES. ¿Qué límites se pueden adivinar solo mirando los datos? ¿Cuál no y por qué?
Solo camioneta no porque sus limites no son nada comunes, ya que es practicamente imposible que hagan un envio que pese mil kg.
- Hay más de cien camionetas para viajes de menos de 2 km, lo que suena a desperdicio. ¿Cuántas tienen una razón clara para ir en camioneta? Para las que no, propongan una explicación.
La unica razon clara para que se haya elegido una camioneta es que las entregas excededieran el limite de peso de los otros tres medios. 

## Para pensar. 
Si les dieran solo el CSV, sin las reglas, ¿podrían reconstruir las reglas del negocio a partir de los datos? ¿Cuáles sí y cuáles no? ¿Qué riesgo hay en dejar que un modelo «descubra» las reglas en lugar de escribirlas a mano?

Las reglas que impiden que el dron vuele de noche, en lluvia, viento fuerte y al centro se pueden deducir a simple vista creo yo. Tal vez definir los limites lleve mas trabajo pero considero que se podrian establecer solo con los datos del csv. Seria de alto riesgo que el modelo descubra o escoja por si mismo ya que debido a algun mal aprendizaje podria proponer a un dron en una entrega con condiciones no aptas.

