           ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
             EXAMEN — MICROSERVICIOS, GATEWAY Y EL MONOLITO
                                CON API
              Tópicos Selectos de Tecnologías Web y Móvil

                            Eduardo Alcaraz
           ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


Nombre: Enrique Martinez___________________________ Calificación :_________


1 — La frase del compañero (10 puntos)
══════════════════════════════════════

  En el pizarrón quedó:

        La API separa clientes del servidor; los microservicios
        separan servidores entre sí.

  Un compañero dice: «Entonces, si mi monolito Django expone una API y
  además lo meto en Docker, ya cumplí las dos mitades de la frase.»

  a) Desarmen su argumento. ¿Qué parte de la frase cree cumplir con la
  API? ¿Qué parte cree cumplir con Docker? ¿En qué se equivoca en cada
  una?

  Solo cumple una mitad de la frase porque el cliente y el servidor están separados por    la API aunque sigue siendo solo un servidor y la parte de docker contiene a todo el Django pero no este seguiría siendo monolito.

  b) Den un contraejemplo mínimo: mismo código Django, *con* API y *con*
  Docker, que *sigamos* pudiendo llamar monolito. ¿Qué tendría que
  añadir (o partir) para que deje de serlo?

  Se podría tomar una parte como las recomendaciones como en el caso de la plataforma de entregas y hacerla independiente del resto de la plataforma. Que se llame a esta por red así cuando tengamos que hacer algún cambio o se presente una falla no afecte a toda la plataforma

  c) ¿La frase del pizarrón habla de *tecnologías* (Docker, REST) o de
  *límites de proceso / despliegue*? Defiendan su lectura con lo que
  vieron en clase.

  Habla de límites de proceso / despliegue, teniendo en cuenta que un servidor se define como algo se ejecuta por separado y se comunican por red. Además de que docker y REST se pueden usar en ambas arquitecturas.

2 — Tres rutas, una trampa (10 puntos)
══════════════════════════════════════

  El equipo muestra este `urls.py' de un solo proyecto Django:

  ┌────
  │ path("usuarios/", ...),
  │ path("pedidos/", ...),
  │ path("recomendar/", ...),
  └────

  y este `docker-compose.yml':

  ┌────
  │ services:
  │   api:
  │     build: .
  │     ports: ["8000:8000"]
  │     deploy:
  │       replicas: 3
  └────

  Afirman: «Tres rutas + tres réplicas = microservicios con alta
  disponibilidad.»

  a) Separen las dos ideas que mezclaron (rutas vs réplicas). ¿Qué
  problema resuelve cada una y cuál *no* resuelve?
  
  Los paths nos sirven para tener una estructura y poder ejecutar partes de la plataforma, pero no son programas independientes. Las réplicas nos ayudan a tener una mayor capacidad en la plataforma, pero no son un microservicio ya que tienen el mismo código y las mismas responsabilidades.

  b) Si una de las tres réplicas se cae a mitad de un `POST /pedidos',
  ¿el sistema dejó de ser monolito? ¿Por qué sí o por qué no?

  Sigue siendo monolito, al caerse la petición debería cancelarse para después reintentar con otra réplica. Las réplicas como su nombre lo dice son copias iguales del mismo código o programa por lo que no son modulos independientes y no se considera microservicio.

  c) Rediseñen *solo con palabras* el `compose' para que sí ilustre
  microservicios (nombres de servicios y responsabilidades; no hace
  falta YAML perfecto). ¿Cuántas *imágenes distintas* mínimo y por qué
  esa cantidad?

  Se necesitaría una imagen que resuelva las peticiones que llegan a la plataforma (gateway), además de 3 imágenes, una para usuarios, otra para pedidos y otra para recomendar. Por lo que propondría al menos 4 imágenes porque se requiere que funcionen por separado y que cualquier modificación o fallo no afecte a las demás.


3 — El gateway que «hace de más» (10 puntos)
════════════════════════════════════════════

  Les proponen este diseño «para no complicar»:

        Un solo contenedor nginx+Python que: valida el JWT, elige
        el medio con el `.joblib', guarda el pedido en SQLite,
        manda el correo y devuelve el HTML.

  Lo llaman «API Gateway».

  a) ¿Es un gateway? Si no, ¿qué es? Usen la analogía del recepcionista
  (o otra) y digan qué oficios mezclaron.

  No es un gateway, es un monolito metido en un contenedor. Un gateway debería funcionar como la recepción de un edificio: revisa quién entra y lo manda a la oficina correcta, pero no hace el trabajo de las oficinas. Aquí se mezclan varios oficios: validar el token, elegir el medio, guardar en SQLite, mandar el correo y armar el HTML.

  b) Mencionen *tres* consecuencias malas de ese diseño cuando el modelo
  pesado se reentrena cada semana y el correo empieza a fallar.

  1. Reentrenar el modelo obliga a reconstruir y reiniciar todo el contenedor, así que cada cambio de modelo tumba también la recepción de pedidos.

  2. Si el correo falla, la petición puede fallar aunque el pedido ya esté guardado, o al revés.

  3. SQLite es un archivo local: no soporta bien varias réplicas escribiendo a la vez y se pierde si el contenedor se recrea sin volumen.

  c) Partan ese contenedor en piezas. Para cada pieza digan: ¿queda en
  el borde (gateway) o detrás? No inventen diez servicios: el mínimo que
  separe borde, logística e (si hace falta) aviso.

  Yo lo partiría así: el gateway solo valida el JWT, reenvía las peticiones y puede servir el HTML (está en el borde). Detrás están Pedidos, que guarda los pedidos en su base de datos; Recomendar, que carga el .joblib y responde la sugerencia; y Avisos, que manda el correo después de que el pedido ya quedó guardado.

4 — `localhost', la trampa favorita (10 puntos)
═══════════════════════════════════════════════

  Pedidos corre en un contenedor. Recomendar en otro, misma Compose.
  Alguien «arregla» la conexión así:

  ┌────
  │ RECOMENDAR_URL=http://127.0.0.1:8002
  └────

  En su laptop, *sin* Docker, ese `curl' a `127.0.0.1:8002' sí
  funcionaba.

  a) Expliquen por qué en Compose ese arreglo suele fallar *aunque*
  Recomendar esté sano. ¿A qué proceso apunta `127.0.0.1' desde dentro
  de Pedidos?

  Dentro de un contenedor, 127.0.0.1 apunta al propio contenedor. Recomendar corre en otro contenedor, así que Pedidos no lo encuentra. En la laptop sin Docker, ambos procesos funcionaban porque compartían el mismo localhost.

  b) ¿Por qué `http://recomendar:8002' sí tiene chance de funcionar?
  ¿Quién «inventa» el nombre `recomendar'?

  Compose crea una red interna y los servicios llevan los nombres definidos en docker-compose.yml. Recomendar es el nombre del servicio y lo define quien escribe el archivo .yml. De esta manera es posible que funcionen las peticiones siempre y cuando esten en la misma red compose.

  c) Ahora Recomendar se muda a la laptop de otro alumno
  (`192.168.0.57'). Escriban la URL que pondrían *y* dos cosas que
  tienen que ser verdad en la WiFi para que no sea teatro (puertos,
  firewall, etc.). Si solo cambian la URL y nada más, ¿qué puede seguir
  fallando?

  http://192.168.0.57:8002. Para que funcione, debe cumplir lo siguiente:

  - El firewall de esa laptop permite entrar al puerto 8002 desde la red local, y la red está en perfil privado.

  Si solo cambian la URL, puede seguir fallando por el firewall, el enlace de escucha, el aislamiento de clientes del WiFi o un cambio de IP por DHCP.

5 — Fallo parcial con números (10 puntos)
═════════════════════════════════════════

  Escenario medido en laboratorio (inventado pero coherente):

  • 1000 `POST /pedidos' por hora en promedio.
  • Recomendar tarda 200 ms cuando está bien.
  • El 5 % del tiempo Recomendar no responde (timeout 3 s).
  • Pedidos, si hay timeout, usa plan B (moto) y responde 200 en 50 ms.
  • El gateway añade 5 ms.

  a) En la hora «normal» (Recomendar bien), ¿el cliente espera ~200 ms o
  ~3 s? ¿Quién pone el tiempo dominante?

  Espera 200 ms, el tiempo dominante lo pone Recomendar. El timeout es solo si Recomendar no responde.
 
  b) En el 5 % malo, con plan B: ¿el cliente ve error o pedido creado?
  ¿Qué «mentira útil» están aceptando (medio quizá no óptimo)?

  El cliente ve pedido creado, después del timeout por la no respuesta de Recomendar, el pedido sale con un medio que quizás no es el óptimo (la moto del plan B). 

  c) Un compañero dice: «Mejor que Pedidos *reintente* 10 veces hasta
  que Recomendar vuelva; así nunca usamos plan B.» ¿Qué le pasa a la
  cola de peticiones y al gateway si Recomendar está caído 10 minutos?
  ¿Plan B siempre es peor que reintentar? Argumenten.

  Reintentar 10 veces con timeout de 3 s hace que cada pedido ocupe hasta 30 s, si Recomendar está caído 10 minutos, se acumulan peticiones en el gateway y en Pedidos, el sistema completo se degrada, incluidos los pedidos que no necesitaban Recomendar. EL plan B no siempre es peor, utilizar la moto es una buena opción a estar esperando que Recomendar regrese a funcionar bien.

6 — Apagan el «edificio equivocado» (10 puntos)
═══════════════════════════════════════════════

  Tres contenedores: gateway, pedidos, recomendar. Hacen tres
  experimentos *por separado*:

  1. `docker compose stop gateway'
  2. `docker compose stop pedidos'
  3. `docker compose stop recomendar'

  Para *cada* experimento digan qué ve el navegador en `http://IP:8080/'
  (página / crear pedido) y qué sigue vivo por dentro. No basta «no
  jala»: digan *qué* no jala y qué sí podría seguir respondiendo si
  alguien hablara por dentro de la red.

  Luego: ¿en cuál de los tres el sistema «parece» más muerto hacia
  afuera aunque más piezas sigan arriba? ¿Qué les enseña eso del borde?

  - stop gateway: el navegador no carga http://IP:8080/. Pedidos y Recomendar siguen vivos y podrían hablar entre sí dentro de la red.

  - stop pedidos: la página sí carga. Al crear pedido, el gateway responde con error porque no tiene a quién enrutar. Recomendar sigue vivo, pero el sistema no puede guardar pedidos.

  - stop recomendar: la página carga y los pedidos se pueden crear, pero sin el medio recomendado (o con el plan B). Es el fallo más tolerable.

El sistema parece más muerto cuando cae el gateway, aunque los otros dos sigan arriba. Demuestra que el borde es un punto único de falla: necesita réplicas y comprobaciones para que el resto del sistema sea útil.

7 — WiFi del salón, conflicto de roles (10 puntos)
══════════════════════════════════════════════════

  Cuatro alumnos:

  • Ana: gateway + HTML
  • Beto: pedidos
  • Carla: recomendar
  • Diana: «yo también levanté un gateway en mi laptop por si Ana falla»

  Todos en la misma WiFi. El cliente (otro equipo) configura a veces la
  IP de Ana y a veces la de Diana.

  a) ¿Qué problema de *diseño* introdujo Diana aunque «todo responda
  200»? (Piensen en una sola puerta vs dos puertas.)

  Diana creó una segunda puerta. Ahora el cliente tiene dos entradas, el estado puede quedar partido entre dos gateways y ninguno sabe lo que hizo el otro. Lo correcto sería tener una puerta principal y en caso de querer una segunda puerta, se puede dejar como una puerta de respaldo.

  b) Beto configuró `RECOMENDAR_URL=http://localhost:8002' porque en su
  máquina desarrolló Pedidos y Recomendar juntos. En el salón Recomendar
  está en la laptop de Carla. ¿Qué falla y cómo lo corrigen *sin* juntar
  otra vez los dos servicios en la laptop de Beto?

  localhost:8002 apunta a la laptop de Beto, donde no corre Recomendar. Se corrige apuntando a la IP de Carla (http://IP_DE_CARLA:8002), con el firewall de Carla abierto y el servicio escuchando en 0.0.0.0. No hace falta juntar servicios en una sola laptop.

  c) La WiFi del campus aísla clientes («AP isolation»). `ping' entre
  alumnos falla. ¿Pueden hacer la práctica tal cual? Si no, propongan
  *un* plan B de laboratorio que preserve la lección «procesos
  separados» (aunque no sea WiFi del salón).

  Con AP isolation no pueden hacer la práctica tal cual. El plan B podría ser correr los tres contenedores en una sola laptop con Compose, cada uno con su nombre de servicio, o usar un router para formar una red local. Lo importante es que cada servicio sea un proceso separado que se comunica por red.

8 — El front que conoce demasiado (10 puntos)
═════════════════════════════════════════════

  El HTML hace esto al enviar el formulario:

  ┌────
  │ await fetch("http://192.168.1.20:8002/sugerir", { ... }); // Recomendar
  │ await fetch("http://192.168.1.30:8001/pedidos", { ... }); // Pedidos
  └────

  El autor dice: «Más rápido: me salto el gateway.»

  a) Listen *tres* problemas (seguridad, cambio de IP, orden de
  llamadas, consistencia del folio, CORS, etc.).

  1. El navegador conoce IPs internas y puertos. Si cambia una IP, el front se rompe.
  
  2. Se exponen servicios internos sin autenticación ni control de acceso; cada uno necesita su propio CORS.

  3. El front orquesta: si Recomendar responde pero Pedidos falla, el estado queda a medias y el front tiene que deshacer cosas.

  b) Rediseñen la secuencia correcta con gateway: *una* llamada desde el
  navegador. ¿Quién habla con Recomendar y por qué no el navegador?

  El navegador hace una sola llamada al gateway. El gateway valida el token, llama a Recomendar desde el servidor (porque Recomendar está en la red interna y no tiene por qué ser público), y después manda los datos a Pedidos, que responde al final.

  Recomendar lo llama el backend porque está en la red interna, no debe ser público y el navegador no debe conocer su existencia ni manejar sus errores.

  c) El selector de modelo (`arbol=|=bosque=|=red') va en el JSON. Si el
  front llama directo a Recomendar *y* a Pedidos, ¿quién debería crear
  el folio para no duplicar lógica? ¿Qué invariante rompen si los dos
  «crean» algo?

  Debe crear el folio Pedidos, porque es el dueño del pedido. Si el front y Pedidos crean folios por separado, se rompe la invariante de un pedido, un folio y un registro. Puede haber folios duplicados o pedidos que no se pueden rastrear.

9 — El LLM vendedor (10 puntos)
═══════════════════════════════

  Producto: tienda + envíos.

  • Modelo `.joblib': medio de transporte.
  • LLM: texto para convencer al cliente en la ficha del producto.

  Un arquitecto propone *un solo* microservicio `cerebro' que: recibe el
  carrito, elige el medio con el árbol *y* genera el pitch de ventas con
  el LLM, todo en la misma petición `/inteligente'.

  a) Critiquen el nombre y el corte. ¿Qué dos oficios distintos
  mezclaron? ¿Qué falla cuando el LLM tarda 8 s y el despacho necesita
  responder en < 500 ms?

  El nombre «cerebro» es vago y el corte mezcla dos oficios: elegir el medio de envío (rápido, con el árbol) y generar el texto de venta (lento, con el LLM). Si el LLM tarda 8 segundos, el despacho también tarda 8, pero el envío necesita responder en medio segundo. Además, si el LLM se cae, se cae el envío también.

  b) Propongan dos endpoints (o dos servicios) y digan cuál usa el
  *front de tienda* y cuál el *flujo de pedido/envío*.

  logistica con POST /envios/medio, que usa el flujo de pedido y envío, y contenido con pitch, que usa el front de tienda.
 
  c) El LLM vive en un server con GPU en otra red. El front de tienda
  ¿apunta a la GPU o al gateway? Si mañana cambian de proveedor LLM
  (otro host), ¿qué archivo/config quieren tocar *una sola vez*?

  El front de tienda apunta al gateway, y el gateway manda la petición a contenido. Solo contenido sabe dónde está la GPU. Si cambian de proveedor de LLM, solo se toca la configuración de contenido.

10 — El inversionista y la semana imposible (10 puntos)
═══════════════════════════════════════════════════════

  Hoy:

  • Panel interno: monolito Django (funciona, poco tráfico).
  • App clientes: gateway + pedidos + recomendar.
  • Idea: LLM de ventas (aún no).
  • Equipo: 5 personas.
  • Inversionista: «Todo a microservicios en 7 días, incluido el panel,
    o no hay dinero.»

  a) Escriban la respuesta al inversionista (máx. 8 líneas) con postura
  *y* riesgo concreto si obedecen a ciegas.

  Partir el panel que ya funciona, sin pruebas ni monitoreo, puede dejar datos separados y al área sin sistema. Lo que proponemos: esta semana ponemos autenticación y límites de uso en el gateway, y sacamos el reentrenamiento del modelo para que no tumbe los pedidos. El panel lo migramos cuando una métrica lo pida. Así bajamos el riesgo y damos resultados en semanas.

  b) Ordenen *estas cuatro* iniciativas de más a menos urgente para
  *esta* semana y justifiquen el orden (no el catálogo soñado):

  1. Partir el panel Django en 6 microservicios.
  2. Sacar el reentrenamiento del `.joblib' a un pipeline que no tumbe
     Pedidos.
  3. Meter auth + rate limit en el gateway público.
  4. Subir el LLM de ventas a producción sin timeouts ni plan B.

  Primero auth y rate limit en el gateway, porque hoy está expuesto. Segundo, sacar el reentrenamiento, porque ya afecta a los pedidos cada semana. Tercero, el LLM a producción, pero solo cuando tenga timeouts y plan B. Y al final, partir el panel, porque es lo más caro y no hace falta por ahora.

  c) Inventen *una* métrica que les diga «ya toca partir X del monolito»
  (no «porque está de moda»). Tiene que ser observable (tiempo, errores,
  despliegues, equipo…).

  Una métrica: si un cambio en un módulo nos obliga a reiniciar otros que no tienen nada que ver más de dos veces al mes, ya toca partirlo.

  d) Cierren con una frase propia (no copien el apunte) que capture:
  ¿microservicios son el objetivo o la herramienta?

  Son la herramienta. Como cualquier cosa puede ser mal usada o ser integrada para intentar venderlo como algo mejor cuando puede ser contraproducente para el entendimiento del sistema que se esta trabajando.
