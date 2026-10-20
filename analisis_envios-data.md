# Analisis de envios-data

## Analisis por archivo

### `envios1.csv`
Es el archivo mas parejo: los cuatro medios aparecen casi igual de seguido, ninguno se lleva la mayoria. Es el caso "ideal" para un arbol, porque tien muchos ejemplos de cada opcion para aprender a distinguirlas. Si algo falla aqui, probablemente no sea por falta de ejemplos.

### `envios2.csv`
Este es el archivo raro. Aparece un medio nuevo, `eskuter`, que no esta en ningun otro archivo, y ademas una parte importante de los envios lo usa (mas o menos 1 de cada 6). La moto y la bicicleta son las mas comunes y el
dron es el que menos sale.
Si el arbol se entreno solo con los cuatro medios de siempre, no conoce `eskuter`, asi que no podra recomendarlo nunca. Eso significa que va a fallar en todos esos envios aunque lo haga bien con el resto. Por eso aqui conviene no asustarse si el resultado sale mas bajo que en otros archivos.

### `envios3.csv`
La moto domina de forma muy clara: casi 3 de cada 4 envios. La camioneta queda en segundo lugar y la bicicleta y el dron aparecen poco, sobre todo el dron.
Aqui hay una trampa: un modelo que respondiera "moto" todo el tiempo ya acertaria muchisimo sin aprender nada. Por eso, si el porcentaje de
aciertos sale alto, no hay que confiarse; hay que ver si tambien logra acertar los medios que casi no aparecen.

### `envios4.csv`
La moto sigue siendo la mas usada, con mas de la mitad de los envios, pero aqui la bicicleta y la camioneta tienen una presencia mucho mas visible que en `envios3`. El dron sigue siendo el menos frecuente.
Es un buen caso para ver si el arbol realmente se fija en las caracteristicas del envio (peso, distancia, etc.) o si se va por lo facil
y recomienda siempre el medio mas comun.

### `envios5.csv`
Esta mas repartido que los anteriores: la moto sigue siendo la mas comun, pero no domina tanto, y la bicicleta tiene una presencia fuerte, casi parecida a la de la moto. La camioneta queda en tercer lugar y el dron sigue siendo el menos frecuente, aunque aqui se ve un poco mas que en otros archivos.
Se espera un comportamiento intermedio: mejor que en los archivos muy desbalanceados, aunque sin llegar a ser tan comodo como `envios1`.

### `envios6.csv`
Es el mas desbalanceado de todos. Casi todo son motos y camionetas, y las bicicletas aparecen muy poco. El dron es practicamente un caso aislado: son tan pocos envios que casi se pierde entre los demas.
Aqui es donde mas probable es que el arbol "se acostumbre" a los medios comunes y tenga muchas dificultades con los raros, sobre todo con el dron. Un buen resultado general en este archivo podria esconder que casi nunca acierta en bicicleta y dron.

## ¿Que podemos esperar del arbol de decision?

Un arbol busca patrones entre las caracteristicas de cada envio (por ejemplo peso, distancia, tamaño o la hora de salida) y el medio que viene marcado como recomendado. Con esto podemos anticipar que:

1. Le ira mejor en los archivos mas parejos y peor en los que dependen de un solo medio.
2. Los medios que casi no aparecen (dron, y a veces bicicleta) seran los mas dificiles de acertar.
3. No sabra manejar `eskuter` si nunca lo vio al entrenar.
4. No hay que quedarse solo con el porcentaje total de aciertos, hay que revisar medio por medio.

Ademas, hay que recordar que el arbol solo aprende de las etiquetas que ya vienen en los CSV. Si esas recomendaciones no son las mas adecuadas en la vida real, el modelo simplemente las va a copiar. Aprende lo que los datos le muestran, no necesariamente lo que seria mejor para cada envio.

# Resultados de la prueba con el arbol de decision

## Resumen general

| Archivo | Aciertos | Lo que mas destaco |
|---------|----------|--------------------|
| envios1 | 95% | Confundio muchos drones con bicicletas |
| envios2 | 78% | No acerto ningun `eskuter` |
| envios3 | 94% | Muy bien con la moto, el dron tuvo muchas falsas alarmas |
| envios4 | 93% | La camioneta y la bicicleta se mandaron a moto a veces |
| envios5 | 93% | Resultado muy parecido a envios4 |
| envios6 | 96% | El mejor total, pero el dron quedo flojo |

## Resultados por archivo

### `envios1.csv`
Acerto 95 de cada 100 envios. La camioneta y la moto salieron casi perfectas. El error principal fue con el dron: unos 450 de los 2,500
drones se clasificaron como bicicleta. Eso indica que el arbol ve a esos dos medios como parecidos en algunos casos (por ejemplo, envios ligeros o de poca distancia). Aun con los datos mas parejos, no fue perfecto.

### `envios2.csv`
Fue el de peor resultado (78%) y se explica con el `eskuter`: no acerto ni uno de los 1,616 envios con ese medio. La mayoria (cerca de 1,400) los mando a moto, que es lo mas parecido que conoce. Esto tambien hizo que la moto pareciera menos confiable de lo que es, porque quedo "contaminada" con esos errores. Si se quitan los eskuter, el arbol acerto cerca del 93% del resto, o sea que con los medios que si conoce funciona bien.

### `envios3.csv`
Acerto 94%. La moto salio muy bien (casi 97 de cada 100). El punto debil fue el dron: encontro casi todos los drones reales, pero tambien llamo "dron" a unas 145 motos, asi que cuando decia dron se equivocaba seguido. La camioneta se confundio con moto en algunos casos (unos 200).

### `envios4.csv`
Acerto 93%. Los errores se repiten: camioneta y bicicleta mandadas a moto (unos 190 y 130 casos) y algunas motos clasificadas como dron. El dron tambien se confundio con bicicleta en unos 90 casos.

### `envios5.csv`
Resultado casi igual al anterior, 93%. La confusion mas grande fue dron contra bicicleta (unos 150 drones se fueron a bicicleta) y moto contra bicicleta (unos 170).

### `envios6.csv`
Tuvo el porcentaje mas alto (96%), pero es engañoso. Como casi todo son motos y camionetas, esos medios inflan el resultado. El dron, que solo tiene 73 envios, quedo como el punto mas flojo: acerto 61, pero llamo "dron" a otros 40 y tantos envios que no lo eran. La bicicleta tambien quedo mas baja (85%).

## ¿Se cumplieron las predicciones?

- **Se cumplio:** el `eskuter` fue un fracaso total en envios2 y bajo el resultado de ese archivo.
- **Se cumplio:** el dron fue el medio mas dificil en casi todos los archivos.
- **Se cumplio a medias:** esperabamos que envios1, el mas parejo, saliera mejor. Salio bien (95%), pero envios6 y envios3 sacaron mas aciertos aunque estan desbalanceados. Esto confirma que el porcentaje total puede enganar: sube cuando hay mucha moto, que es facil de acertar.
- **No fue tan grave como se esperaba:** en los archivos desbalanceados el arbol si reconocio a los medios chicos (dron y bicicleta) en la mayoria de los casos. Su problema fue mas bien el contrario: llamar "dron" a cosas que no lo eran.

## Patrones que se repiten

1. **La camioneta casi nunca se predice por error.** Cuando el arbol dice "camioneta", casi siempre tiene razon. Pero a veces la manda a moto, y por eso se le escapan unas 7 a 15 de cada 100.
2. **La moto es el "cajon" donde caen los errores.** Muchos envios de otros medios terminan clasificados como moto.
3. **Dron y bicicleta se confunden entre si.** Probablemente tengan caracteristicas parecidas en algunos envios.
4. **El arbol no inventa medios nuevos.** Solo reconoce lo que vio al entrenar.

## Conclusiones

El arbol funciona bastante bien en general (entre 92% y 96% en los archivos que usan los 4 medios conocidos), pero no hay que quedarse con
ese numero. Lo mas importante es lo que pasa medio por medio: el dron y la bicicleta son los mas inestables y la moto absorbe muchos errores. Ademas, el modelo solo aprende de las etiquetas que ya traen los CSV, asi que no significa que sus recomendaciones sean las mejores en la vida real, solo que copia bien los patrones de los datos.