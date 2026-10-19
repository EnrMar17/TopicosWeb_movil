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

# Actividad 2 — La hora y el dron

## Predicciones

- En teoria no deberian salir drones a las 3 am, ya que en las reglas se establece que los drones no pueden salir de noche.
- Creo que estaria entre un 20% o 25% los envios de noche.

## Resultados

### Medios recomendados por hora

| Hora de salida | Bicicleta | Camioneta | Dron | Moto |
|---|---:|---:|---:|---:|
| 0 | 2 | 12 | 0 | 63 |
| 1 | 6 | 11 | 0 | 49 |
| 2 | 5 | 19 | 0 | 59 |
| 3 | 4 | 13 | 0 | 60 |
| 4 | 2 | 10 | 0 | 47 |
| 5 | 8 | 25 | 0 | 116 |
| 6 | 94 | 50 | 33 | 136 |
| 7 | 204 | 92 | 68 | 233 |
| 8 | 205 | 118 | 57 | 252 |
| 9 | 187 | 97 | 65 | 279 |
| 10 | 192 | 123 | 68 | 273 |
| 11 | 178 | 107 | 72 | 283 |
| 12 | 217 | 111 | 82 | 297 |
| 13 | 211 | 112 | 70 | 284 |
| 14 | 204 | 103 | 72 | 274 |
| 15 | 199 | 122 | 81 | 303 |
| 16 | 213 | 108 | 59 | 260 |
| 17 | 192 | 97 | 69 | 292 |
| 18 | 162 | 97 | 72 | 248 |
| 19 | 166 | 78 | 45 | 199 |
| 20 | 115 | 72 | 35 | 160 |
| 21 | 20 | 58 | 0 | 240 |
| 22 | 5 | 28 | 0 | 116 |
| 23 | 5 | 15 | 0 | 55 |

### Cantidad de envios por horario

| Horario | Cantidad de envios | Porcentaje |
|---|---:|---:|
| Dia | 8,947 | 89.47 % |
| Noche | 1,053 | 10.53 % |
| **Total** | **10,000** | **100 %** |

### Medios recomendados por horario

| Horario | Bicicleta | Camioneta | Dron | Moto |
|---|---:|---:|---:|---:|
| Dia | 2,739 | 1,487 | 948 | 3,773 |
| Noche | 57 | 191 | 0 | 805 |

### Porcentaje de medios por horario

| Horario | Bicicleta | Camioneta | Dron | Moto |
|---|---:|---:|---:|---:|
| Dia | 30.61 % | 16.62 % | 10.60 % | 42.17 % |
| Noche | 5.41 % | 18.14 % | 0.00 % | 76.45 % |

### Bicicletas y motos a las 20:00 y 21:00

| Hora de salida | Bicicleta | Moto |
|---|---:|---:|
| 20:00 | 115 | 160 |
| 21:00 | 20 | 240 |

## Comparación con las predicciones

- Acerte porque no hay salida de drones a las 3 am.
- Falle, el porcentaje de envios en la noche es de 10.53% en contra al 20% que predije.

## Preguntas

- ¿En qué horas no hay ningún dron? ¿Coincide con la regla?
El dron no aparece a las 0, 1, 2, 3, 4, 5, 21, 22 y 23 horas, acorde a la regla de no usarlo en la noche.
- ¿Cuántos envíos son nocturnos y cuántos diurnos? ¿Qué aprende el modelo de esa distribución?
Hay 1,053 envios nocturnos, equivalentes al 10.53 %, y 8,947 envios diurnos, equivalentes al 89.47 %.
El modelo puede aprender que la mayoria de los envios ocurre durante el dia y que el dron no se utiliza durante la noche.
- ¿Por qué entre las 20:00 y las 21:00 casi desaparecen las bicicletas y aumentan las motos?
En teoria en las reglas se establece una penalizacion para las bicicletas si se eligen en la noche, pero no se impide su eleccion.
- ¿Por qué a un árbol de decisión le cuesta representar la condición «de noche»?
Porque de noche se establece con dos intervalos, seria mas sencillo si de noche se estableciera en una sola variable.

## Para pensar

- ¿Qué nueva columna ayudaría al árbol a identificar los envíos nocturnos?
Se puede agregar una columna llamada `es_de_noche`, con valor 1 para los envios realizados antes de las 6:00 o a partir de las 21:00, y valor 0 para los demas.

# Actividad 3 — Anatomia de los errores

## Predicciones

- Por su similitud, la confusion mas frecuentre deberia ser entre las motos y bicicletas.
- Puede ser posible pero considero que no lo hara.

## Resultados

### Total de errores vs envios de prueba

| Resultado | Cantidad |
|---|---:|
| Envíos de prueba | 2,000 |
| Errores totales | 158 |
| Porcentaje de errores | 7.90 % |

### Tres confusiones mas frecuentes

| Medio real | Medio predicho | Casos |
|---|---|---:|
| Moto | Bicicleta | 46 |
| Camioneta | Moto | 32 |
| Moto | Dron | 29 |

### Motos clasificacdas como drones 

| Resultado | Cantidad |
|---|---:|
| Total de casos | 29 |
| De noche | 26 |
| De día | 3 |

### Distancia de motos clasificadas como bicicletas

| Medida | Distancia |
|---|---:|
| Cantidad de envíos | 46 |
| Distancia mínima | 1.35 km |
| Distancia promedio | 4.08 km |
| Distancia máxima | 6.89 km |

## Comparacion con las predicciones

- Acerte en que las motos y bicicletas iban a ser los medios mas confundidos.
- No se confundio ninguna bicicleta con camioneta pero si camioneta con bicicleta.

## Preguntas 

- ¿Cuántos errores hay y cuáles son las tres confusiones más frecuentes? ¿Son entre medios parecidos o muy distintos? ¿Qué les dice eso?
De los 2,000 envíos de prueba, el modelo cometió 158 errores, lo que representa un 7.9 %.
Las tres confusiones más frecuentes fueron: moto a bicicleta, camioneta a moto y moto a dron.
Esto indica que el modelo puede reconocer correctamente la mayoría de los envíos, pero algunas características de los paquetes se parecen entre distintos medios y dificultan su clasificación.
- Revisen los envíos que eran moto y el modelo mandó a dron. ¿Cuántos son de noche? ¿Cuáles corregirían las reglas del negocio y cuáles no? ¿Qué tienen en común los que no?
Se encontraron 29 envíos de moto clasificados como drones. De estos, 26 ocurrieron de noche y 3 durante el día.
Las reglas del negocio rechazaron los 26 casos nocturnos, ya que no cumplían las condiciones para utilizar un dron. Estos casos deberían corregirse para evitar asignar un medio que no está permitido por las reglas. Los otros 3 casos sí cumplían las condiciones de las reglas para utilizar un dron, por lo que estas no los rechazarían automáticamente. Eran envíos diurnos, con poco peso y volumen reducido.
Esto demuestra que una predicción incorrecta no siempre incumple las restricciones del negocio. El modelo puede equivocarse respecto al medio original aunque el medio que predice sea viable según las reglas establecidas.
- Revisen los envíos que eran moto y el modelo mandó a bicicleta. ¿Están cerca del límite de 7 km? Si no es la distancia, busquen qué columnas los distinguen de las bicicletas que el modelo sí acertó.
Se encontraron 46 envíos de moto clasificados como bicicletas. Sus distancias iban de 1.35 a 6.89 km, con un promedio de 4.08 km. Todos estaban dentro del límite de 7 km, pero no todos estaban cerca de ese límite.
Al comparar sus características con las bicicletas clasificadas correctamente, los promedios de peso, volumen y dimensiones fueron bastante similares. Por eso, la distancia y las características físicas del paquete no parecen explicar por sí solas todos los errores.
Las diferencias más notables aparecieron en la prioridad y el clima:
- El 47.8 % de las motos confundidas tenía prioridad `mismo_dia`, frente al 11.9 % de las bicicletas acertadas.
- El 23.9 % de las motos confundidas correspondía a envíos con lluvia, frente al 2.0 % de las bicicletas acertadas.
- El 23.9 % de las motos confundidas tenía viento fuerte, frente al 13.2 % de las bicicletas acertadas.

### Para pensar

Si solo pudiéramos corregir un tipo de error, elegiríamos las motos clasificadas como bicicletas, porque fue la confusión más frecuente, con 46 casos.
Primero revisaríamos las reglas del negocio para determinar si la prioridad y el clima deben influir directamente en la elección del medio. Si esas condiciones son importantes, las incorporaríamos explícitamente a las reglas. Después, si fuera necesario, mejoraríamos los datos de entrenamiento y volveríamos a entrenar el modelo.
No bastaría con modificar el límite de distancia, porque todos los casos analizados estaban dentro de los 7 km y sus distancias eran variadas.

# Actividad 4 — ¿Que columnas usa de verdad el modelo?

## Predicciones

1. distancia_km.
2. peso_kg.
3. volumen_l.
4. refrigerado.
5. clima.
6. hora_salida.
7. valor_declarado_mxn.
8. largo_cm.
9. ancho_cm.
10. alto_cm.
11. zona_destino.
12. prioridad.
13. fragil.
14. trafico.

## Resultados

La exactitud original del modelo fue de **92.10 %**. Las importancias de las columnas fueron las siguientes:

| Columna | Importancia |
|---|---:|
| `distancia_km` | 0.3220 |
| `volumen_l` | 0.1929 |
| `clima` | 0.1438 |
| `refrigerado` | 0.1313 |
| `peso_kg` | 0.1263 |
| `hora_salida` | 0.0587 |
| `fragil` | 0.0199 |
| `prioridad` | 0.0031 |
| `valor_declarado_mxn` | 0.0007 |
| `ancho_cm` | 0.0007 |
| `largo_cm` | 0.0003 |
| `alto_cm` | 0.0003 |
| `trafico` | 0.0002 |
| `zona_destino` | 0.0000 |

| Columna eliminada | Exactitud sin la columna | Cambio |
|---|---:|---:|
| `distancia_km` | 79.30 % | -12.80 |
| `clima` | 84.45 % | -7.65 |
| `refrigerado` | 87.85 % | -4.25 |
| `hora_salida` | 89.10 % | -3.00 |
| `peso_kg` | 90.40 % | -1.70 |
| `volumen_l` | 90.60 % | -1.50 |
| `fragil` | 91.55 % | -0.55 |
| `largo_cm` | 92.05 % | -0.05 |
| `alto_cm` | 92.05 % | -0.05 |
| `ancho_cm` | 92.05 % | -0.05 |
| `zona_destino` | 92.10 % | 0.00 |
| `valor_declarado_mxn` | 92.10 % | 0.00 |
| `trafico` | 92.10 % | 0.00 |
| `prioridad` | 92.15 % | +0.05 |

## Comparacion con las predicciones

Falle

## Preguntas

- ¿Cuáles son las cuatro columnas más importantes? ¿Coinciden con las primeras preguntas del árbol del paso 8? ¿Y con su predicción?
Las cuatro columnas más importantes son `distancia_km`, `volumen_l`, `clima` y `refrigerado`. La distancia es la más importante, con un valor de 0.3220.
Estas columnas representan características que ayudan al árbol a distinguir qué medio de transporte conviene utilizar. La distancia y el volumen permiten evaluar el recorrido y el tamaño del paquete, mientras que el clima y la refrigeración también influyen en la elección.
- ¿Qué columna, al quitarla, baja más la exactitud? ¿Cuáles no la cambian nada?
La columna cuya eliminación más perjudicó al modelo fue `distancia_km`: la exactitud bajó de 92.10 % a 79.30 %, una disminución de 12.80 puntos porcentuales.
Las columnas que no cambiaron la exactitud fueron `zona_destino`, `valor_declarado_mxn` y `trafico`. Al eliminar `prioridad`, la exactitud incluso aumentó ligeramente, de 92.10 % a 92.15 %.Esto demuestra que no todas las columnas aportan la misma información al modelo. Sin embargo, una importancia baja o nula no significa necesariamente que el dato carezca de utilidad para otras funciones de la plataforma.
- La zona de destino tiene importancia cero, pero en la actividad 1 vieron que el dron nunca va al centro. ¿Cómo puede ser que el modelo no use la zona y, aun así, la plataforma nunca mande un dron al centro?
Esto ocurre porque el modelo de aprendizaje automático y las reglas del negocio pueden funcionar de manera independiente. Aunque el árbol no utilice `zona_destino` para realizar sus predicciones, la aplicación puede tener una regla que impida enviar drones al centro.

## Para pensar

Si el modelo no utiliza algunas de las catorce columnas, no necesariamente deberíamos dejar de solicitarlas. Primero debemos comprobar si se necesitan para las reglas del negocio, para registrar información de los envíos o para otras funciones de la aplicación.
Si una columna no ayuda a predecir el medio ni tiene otra utilidad, podríamos considerar eliminarla para simplificar el formulario. Sin embargo, si es necesaria para validar restricciones, como la zona de destino, debemos conservarla aunque su importancia para el modelo sea cero.

# Actividad 5 — El dron es minoría: ¿hay que balancear el dataset?

## Parte A — Pensar antes de tocar los datos

- ¿Qué exactitud tendría un modelo que nunca dice dron y siempre acierta todo lo demás? ¿Y uno que siempre dice moto? ¿Qué nos dice eso sobre usar la exactitud para juzgar un dataset desbalanceado? ¿Qué medidas usaríamos en su lugar?
Un modelo que nunca predice dron y clasifica correctamente todos los envíos de las demás clases tendría una exactitud de 90.52 % en el dataset completo y 90.50 % en la prueba. En cambio, un modelo que siempre predice moto tendría una exactitud de 45.78 % en el dataset completo y 45.75 % en la prueba.

| Modelo hipotético | Dataset completo | Prueba |
|---|---:|---:|
| Nunca predice dron y acierta las demás clases | 90.52 % | 90.50 % |
| Siempre predice moto | 45.78 % | 45.75 % |

Esto demuestra que la exactitud por sí sola puede ser engañosa, porque un modelo puede obtener un porcentaje alto sin detectar correctamente los envíos de dron. Por eso también debemos revisar la **precision, el recall y el F1-score** de esa clase. La precision indica cuántas predicciones de dron fueron correctas, mientras que el recall indica cuántos de los drones reales logró detectar el modelo.
- ¿Por qué hay tan pocos drones? ¿Es un error de los datos o refleja cómo funciona la empresa? ¿Cambia eso la decisión de balancear?
Que solo el 9.5 % de los envíos sean de dron no significa necesariamente que exista un error en los datos. Puede reflejar la operación real de la empresa, ya que los drones podrían utilizarse únicamente en determinadas condiciones de distancia, peso, clima, horario o tipo de envío.
Esto sí influye en la decisión de balancear. Si la proporción representa la realidad, no conviene modificarla sin evaluar las consecuencias. Sin embargo, podemos probar técnicas de balanceo para comprobar si el modelo detecta más drones y si ese beneficio compensa los errores adicionales.
- Si decidimos balancear, ¿se hace antes o después de separar los datos de entrenamiento y prueba? ¿Se balancea también la prueba?
Primero debemos separar los datos en entrenamiento y prueba. Después, aplicamos el balanceo únicamente a los datos de entrenamiento.
Los datos de prueba no deben balancearse, porque deben representar la distribución real de los envíos y mantenerse iguales para todas las estrategias. Si balanceamos la prueba, los resultados dejan de representar correctamente el funcionamiento esperado de la plataforma y la comparación entre modelos deja de ser justa.

---

## Parte B — Probar estrategias

Para comparar las estrategias se utilizaron los mismos **2,000 envíos de prueba**, sin modificarlos. El modelo original obtuvo una exactitud de 92.10 %.

Se probaron tres estrategias: submuestreo, sobremuestreo y ponderación de clases mediante `class_weight="balanced"`.

### Resultados de la comparación

| Estrategia | Envíos de entrenamiento | Exactitud | Precision dron | Recall dron | Veces que predice dron | Sugerencias imposibles |
|---|---:|---:|---:|---:|---:|---:|
| Sin balancear | 8,000 | 92.10 % | 83.90 % | 90.53 % | 205 | 31 |
| Submuestreo | 3,032 | 89.75 % | 88.94 % | 93.16 % | 199 | 29 |
| Sobremuestreo | 14,652 | 90.65 % | 76.61 % | 100.00 % | 248 | 35 |
| `class_weight="balanced"` | 8,000 | 90.25 % | 76.61 % | 100.00 % | 248 | 35 |

En la prueba había **190 drones reales**.

### Detalle de los resultados del dron

| Estrategia | Drones detectados | Drones no detectados | Predicciones de dron incorrectas |
|---|---:|---:|---:|
| Sin balancear | 172 | 18 | 33 |
| Submuestreo | 177 | 13 | 22 |
| Sobremuestreo | 190 | 0 | 58 |
| `class_weight="balanced"` | 190 | 0 | 58 |

### Interpretación de las estrategias

**1. Sin balancear**

El modelo original obtuvo la mayor exactitud, con 92.10 %. Detectó 172 de los 190 drones reales, aunque dejó pasar 18. Es una buena referencia porque aprende con la distribución original de los datos.

**2. Submuestreo**

Se redujeron las clases mayoritarias hasta dejar 3,032 registros de entrenamiento. La precision del dron aumentó a 88.94 % y el recall a 93.16 %. Además, las sugerencias imposibles bajaron a 29.
El inconveniente es que se eliminaron **4,968 ejemplos, equivalentes al 62.10 % del entrenamiento**. Esto puede hacer que el modelo pierda información útil sobre las clases mayoritarias y sus diferentes condiciones.

**3. Sobremuestreo**

Se repitieron ejemplos de las clases minoritarias para aumentar su representación durante el entrenamiento. El modelo detectó los 190 drones reales, por lo que obtuvo un recall de 100 %. Sin embargo, también clasificó incorrectamente 58 envíos como drones, lo que redujo la precision a 76.61 %.

Esto significa que el modelo logró detectar todos los drones del conjunto de prueba, pero también recomendó este medio en casos donde no correspondía.

**4. Ponderación de clases**

Con `class_weight="balanced"`, se dio mayor importancia a los errores de las clases menos representadas durante el entrenamiento. En este experimento se obtuvieron los mismos resultados que con el sobremuestreo: recall de 100 %, precision de 76.61 % y 248 predicciones de dron.

Aunque ambas técnicas funcionan de manera diferente, en esta ejecución produjeron los mismos resultados. Esto no significa que siempre vayan a comportarse igual, ya que su efecto depende de los datos y de la configuración del modelo.

### Comparación del F1 macro

| Estrategia | F1 macro |
|---|---:|
| Sin balancear | 91.24 % |
| Submuestreo | 89.74 % |
| Sobremuestreo | 89.80 % |
| `class_weight="balanced"` | 89.49 % |

El modelo sin balancear obtuvo el F1 macro más alto, con 91.24 %. Esto indica que mantuvo el mejor equilibrio general entre precision y recall de las distintas clases en este experimento, aunque dejó de detectar 18 de los 190 drones reales.

Por lo tanto, balancear el dataset no mejoró todas las métricas. El submuestreo y el sobremuestreo modificaron el comportamiento del modelo, pero el modelo original conservó el mejor resultado general según el F1 macro.

### Trampa deliberada: balancear antes de separar los datos

Para comprobar qué sucede al realizar el balanceo incorrectamente, se balanceó el dataset completo antes de dividirlo en entrenamiento y prueba. Como consecuencia, algunas filas de prueba tenían características idénticas a las de filas del conjunto de entrenamiento.

| Resultado | Valor |
|---|---:|
| Filas de entrenamiento | 14,649 |
| Filas de prueba | 3,663 |
| Filas de prueba con características idénticas a alguna de entrenamiento | 2,911 |
| Exactitud | 91.51 % |
| Precision de dron | 89.66 % |
| Recall de dron | 97.49 % |
| Veces que predice dron | 996 |
| Sugerencias imposibles | 65 |

Estos resultados muestran que existe un solapamiento de características entre los conjuntos de entrenamiento y prueba. Esto puede hacer que la evaluación sea menos confiable, porque el conjunto de prueba contiene ejemplos con características que el modelo ya encontró durante el entrenamiento.

En esta ejecución, la exactitud fue de 91.51 %, inferior al 92.10 % del modelo sin balancear. Por lo tanto, balancear antes de separar los datos no necesariamente aumenta la exactitud; el problema es que puede producir una evaluación menos representativa del desempeño con envíos nuevos.

La forma correcta es separar primero los datos en entrenamiento y prueba y aplicar el balanceo únicamente al conjunto de entrenamiento. Así se evita que la preparación de los datos introduzca solapamientos innecesarios y se conserva una evaluación más confiable.

---

## Parte C — Interpretar

- ¿Qué pasó con el recall del dron y qué pasó con su precision? ¿Por qué una sube cuando la otra baja?

El recall aumentó con las estrategias de balanceo. Con el sobremuestreo y `class_weight="balanced"` llegó al 100 %, porque el modelo detectó los 190 drones reales. Sin embargo, la precision bajó de 83.90 % a 76.61 %, ya que también clasificó incorrectamente como dron algunos envíos que pertenecían a otras clases.
Esto sucede porque el modelo se vuelve más propenso a predecir dron. Así reduce los drones que deja pasar, pero aumenta las falsas alarmas. El submuestreo obtuvo un resultado más equilibrado: precision de 88.94 % y recall de 93.16 %.

- ¿Alguna estrategia dejó al modelo con muchos menos datos de entrenamiento? ¿Qué se pierde con eso?

Sí, el submuestreo redujo el entrenamiento de 8,000 a 3,032 registros, eliminando 4,968 ejemplos, equivalentes al 62.10 %.
Al quitar tantos registros, se puede perder información sobre las características y las condiciones de los envíos de bicicleta, camioneta y moto. Esto puede dificultar que el modelo aprenda correctamente las diferencias entre esas clases.

- Si dos estrategias distintas dieron números casi iguales para el dron, ¿por qué son, en el fondo, la misma idea?

El sobremuestreo y `class_weight="balanced"` obtuvieron resultados iguales en este experimento: ambos alcanzaron un recall de 100 %, una precision de 76.61 % y 248 predicciones de dron.
Ambas estrategias buscan que el modelo preste más atención a la clase minoritaria, aunque lo hacen de maneras diferentes: el sobremuestreo repite ejemplos y class_weight modifica el peso de los errores durante el entrenamiento. El sobremuestreo lo hace repitiendo ejemplos de dron, mientras que `class_weight` aumenta el costo de equivocarse al clasificar esa clase. Aunque el mecanismo es diferente, en este caso ambos provocaron un comportamiento muy parecido.

- Después de balancear, ¿la confianza del 84 % sigue significando lo mismo?

No necesariamente. Al balancear los datos, cambia la proporción de ejemplos de dron que el modelo ve durante el entrenamiento. Por eso, el porcentaje de confianza que muestra el árbol no debe interpretarse automáticamente como la probabilidad real de que una recomendación sea correcta.
Si la plataforma utiliza un porcentaje de confianza, convendría comprobar si está bien calibrado con datos de prueba que mantengan la distribución real de los envíos. De lo contrario, podría mostrar una confianza que no representa correctamente lo que sucede en la empresa.

---

## Parte D — Decidir

- ¿La empresa debería utilizar el modelo balanceado en la plataforma?

No recomendaría sustituir directamente el modelo original por uno balanceado sin realizar más pruebas. En este experimento, el modelo sin balancear obtuvo la mayor exactitud, con 92.10 %, y también el mayor F1 macro, con 91.24 %.

El sobremuestreo y `class_weight="balanced"` lograron detectar todos los drones reales, pero su precision bajó a 76.61 % y generaron 58 predicciones de dron incorrectas. Esto podría ocasionar recomendaciones innecesarias y afectar la operación. Por otro lado, el submuestreo obtuvo una precision mayor, de 88.94 %, y un recall de 93.16 %, aunque perdió una gran cantidad de ejemplos de entrenamiento.

La decisión también depende del costo de los errores. Si es muy costoso dejar pasar un envío que sí podría realizarse con dron, conviene dar más importancia al recall. Si enviar un dron cuando no corresponde implica riesgos, gastos o incumplimiento de las reglas, también es importante mantener una precision alta.

Las reglas del negocio pueden corregir algunas recomendaciones imposibles, por ejemplo, cuando un dron no está permitido por el horario o las condiciones del envío. Sin embargo, no necesariamente corrigen todos los errores de clasificación: una recomendación puede ser posible según las reglas y aun así no ser la opción más conveniente.

Si la empresa compra el doble de drones, podría aumentar la cantidad de envíos que pueden realizarse con ellos. En ese caso, convendría actualizar los datos y volver a evaluar el modelo, porque la distribución y las condiciones de operación podrían cambiar.

**Conclusión:** por ahora, mantendría el modelo sin balancear como referencia y probaría el submuestreo como alternativa. Antes de implementar cualquiera de los modelos, compararía sus resultados con las reglas del negocio y el costo real de las recomendaciones incorrectas. No se trata de detectar la mayor cantidad posible de drones a cualquier precio, sino de recomendar ese medio cuando realmente convenga.
