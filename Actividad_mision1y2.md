
# Problema Universidad

## Enrique Martínez

### Problema

Una universidad pública mantiene el alta de materias, el pago de inscripción, las constancias y las becas en **decenas de páginas sueltas** (PHP, ASP clásico y un par de servicios nuevos). Se requiere un **portal web único** para el siguiente ciclo.

El estado actual, documentado por control escolar y por caja, es el siguiente.

1. Cada trámite es un archivo distinto. En todos se copia el mismo bloque de «¿hay sesión?», el mismo registro en bitácora y el mismo encabezado HTML. Cuando cambia la regla de caducidad de la sesión, hay que tocar cuarenta archivos; siempre se olvida uno.

2. El pago de inscripción admite **tarjeta, transferencia SPEI y referencia de ventanilla**. El script de `pagar.php` es un `switch` de doscientas líneas. Cada banco nuevo obliga a editar ese archivo. El protocolo de un banco habla de «créditos» y códigos `00/01`; el reglamento interno habla de «pago de inscripción» y estados `pendiente / acreditado / rechazado`.

3. La plantilla del kardex ejecuta consultas SQL para armar la tabla de calificaciones. Los reportes de constancias duplican esas consultas con otro formato.

4. Cuando el pago se acredita, el mismo script llama a control escolar (alta de materias), dispara un correo al estudiante y avisa a caja. Si el correo falla, a veces no se registra el alta. Si el estudiante pulsa dos veces «pagar» porque la página tarda, se han cobrado **dos** cargos.

5. La **aplicación móvil** de la universidad y el **kiosco** de la biblioteca deben mostrar el mismo trámite. La app pide un JSON mínimo (folio, saldo, plazo). El kiosco pide una página HTML con el escudo y la tabla de vencimientos. Hoy el equipo de la app hace **doce peticiones** para pintar la pantalla de inicio.

6. El servicio de un banco y el de un validador de CURP externo **se caen** con frecuencia. Mientras no responden, el estudiante ve la rueda de espera y no puede ni consultar el kardex, que no depende de esos colaboradores.

7. Un proveedor propone, para la descarga de una constancia en PDF, Event Sourcing, CQRS, una malla de microservicios y un almacén global Redux en el navegador. El trámite de la constancia es: autenticar, consultar un registro ya existente y generar un archivo.

El portal nuevo puede construirse en Spring, en Laravel o en Express: el análisis de patrones **no** espera un marco concreto. Sí espera que se use lo que el marco ya instancia (enrutador, middleware, transacción del ORM) y que no se copie un diagrama UML al lado.

### Misión 1 - El portal no es un patrón

Enuncie **seis** problemas distintos del relato (un renglón cada uno). Para cada uno indique:

- la **capa** (presentación, políticas transversales, aplicación/dominio, datos, integración);
- el **patrón** (o la pareja de patrones) que corresponde;
-  **por qué ese** y no el vecino más fácil de confundir (por ejemplo Adapter frente a Facade, Observer frente a Unit of Work);
-  **cuándo no** aplicaría, aunque el nombre «quede bonito».

| Problema | Capa | Patrón | Por qué ese y no el vecino? | Cuando no aplicaría? |
|----------|------|--------|-----------------------------|----------------------|
| Cada trámite está en un archivo distinto y se repiten cosas como revisar la sesión y guardar la bitácora. | Políticas transversales | Front Controller, Chain of Responsibility | Front Controller deja una entrada común para las peticiones y la cadena permite hacer las revisiones una tras otra. Un Page Controller no resolvería el problema porque cada página seguiría manejando sus validaciones por separado. | Si una regla solo pertenece a un trámite específico, no tiene sentido meterla en toda la cadena. Tampoco hay que crear un Front Controller propio si el framework ya trae router y middleware. |
| `pagar.php` tiene un `switch` enorme para tarjeta, SPEI y ventanilla, además de que los bancos manejan códigos y palabras diferentes a las de la universidad. | Aplicación/dominio, Integración | Strategy, Adapter | Strategy nos sirve para cambiar la forma de pago sin seguir aumentando el `switch`, mientras que Adapter traduce lo que manda el banco a algo que entiende la universidad. Facade no serviría igual porque aquí sí necesitamos hacer una traducción. | Si solo existiera una forma de pago, Strategy sería innecesario. Adapter tampoco haría falta si el banco ya hablara exactamente el mismo lenguaje que el sistema. |
| La plantilla del kardex ejecuta SQL y las constancias terminan repitiendo esas mismas consultas para mostrarlas de otra manera. | Datos, Presentación | Repository, Template View | Repository deja las consultas fuera de la vista y Template View se preocupa solo por mostrar la información. Usar únicamente MVC no quitaría el problema de tener SQL metido en la plantilla. | Si fuera una consulta sencilla usada una sola vez y sin posibilidad de repetirse, crear demasiadas clases alrededor de ella podría ser más complicado que útil. |
| Cuando se acredita un pago deben quedar registrados correctamente el cobro y el alta, y después se debe avisar por correo y a caja. | Datos, Aplicación | Unit of Work, Observer | Unit of Work se encarga de que los cambios importantes se guarden juntos y Observer sirve después para avisar a los demás. Observer solo no basta porque puede mandar el aviso aunque algo no haya quedado bien guardado. | Unit of Work no hace falta en operaciones que solo consultan información. Observer tampoco tiene sentido si no hay otros componentes interesados en reaccionar al evento. |
| La app y el kiosco usan el mismo trámite, pero la app quiere un JSON pequeño y el kiosco necesita más información y HTML. Además, la app hace doce peticiones para cargar su inicio. | Borde / Integración | BFF | BFF permite darle a cada cliente justo la información que necesita y así la app no tiene que hacer tantas peticiones. No usamos Factory porque aquí no estamos creando objetos, sino preparando una interfaz diferente para cada cliente. | Si la app, el kiosco y la web necesitaran exactamente la misma información, un BFF separado sería una capa extra sin beneficio. |
| El banco y el validador de CURP se caen seguido y hacen que el usuario se quede esperando, incluso al consultar cosas que no dependen de ellos, como el kardex. | Integración | Timeout, Circuit Breaker | Timeout evita que el usuario se quede esperando demasiado y Circuit Breaker deja de llamar por un rato si el servicio ya está fallando. Solo hacer reintentos podría empeorar el problema. | No hace falta utilizarlos para operaciones locales o dependencias que no pueden provocar una falla en cadena. Tampoco se deberían reintentar errores que claramente no son temporales. |

### Misión 2 - Una petición, varios patrones

Siga el caso de uso  **pagar la inscripción**  desde el clic (o desde  `POST`) hasta persistir y notificar. Liste,  **en orden**, las estructuras que atraviesa la petición. Para cada paso: qué objeto o mecanismo es (enrutador, filtro, servicio, repositorio…) y  **qué patrón**  está realizando.

Apóyese en el esquema de composición a lo largo de una petición HTTP del apartado web. No invente una capa vacía que solo delega.

| Paso | Mecanismo u objeto | Patrón que realiza | 
|------|--------------------|--------------------| 
| 1 | El estudiante selecciona la forma de pago y la pantalla prepara datos como folio, monto y método. | MVC / MVVM / flujo unidireccional | 
| 2 | Al presionar **Pagar**, el cliente envía la operación como una petición `POST /pagos` mediante HTTP. | — | 
| 3 | Si la petición viene de la app o del kiosco, en el borde se puede ajustar la respuesta a lo que necesita cada cliente. Si hay varios servicios detrás, también se pueden concentrar políticas comunes de entrada. | BFF / API Gateway | 
| 4 | La petición entra al portal por el enrutador principal y se manda hacia el controlador encargado del pago. | Front Controller | 
| 5 | Antes de llegar al controlador, la petición pasa por validaciones como sesión, autenticación y bitácora. Si alguna falla, el proceso puede detenerse ahí. | Chain of Responsibility | 
| 6 | El controlador recibe el `POST`, obtiene los datos enviados y llama al caso de uso. No debería decidir cómo cobra cada banco ni escribir SQL directamente. | Page Controller | 
| 7 | Se ejecuta algo como `pagarInscripcion(estudianteId, metodo, monto)`. Aquí se coordinan las reglas principales del trámite, por ejemplo revisar saldo, periodo y evitar procesar dos veces el mismo folio. | Service Layer | 
| 8 | Según el método elegido por el estudiante se usa el algoritmo correspondiente para tarjeta, SPEI o ventanilla, evitando el `switch` enorme de `pagar.php`. | Strategy | 
| 9 | Si se necesita hablar con un banco, se traduce su protocolo al lenguaje de la universidad. Por ejemplo, un código `00` puede convertirse en estado `acreditado`. | Adapter | 
| 10 | La llamada al banco se protege con un tiempo máximo de espera y, si el servicio lleva varios fallos, se deja de insistir temporalmente para no afectar todo el portal. | Timeout + Circuit Breaker | 
| 11 | Con el resultado del cobro, el sistema consulta o modifica los datos mediante objetos como `PagoRepository` o `InscripcionRepository`, en lugar de tener SQL dentro del controlador o la vista. | Repository | 
| 12 | Los cambios que deben quedar juntos, como registrar el pago acreditado y el alta correspondiente, se guardan dentro de una misma transacción. Si algo falla antes de terminar, se revierten los cambios. | Unit of Work | 
| 13 | Una vez confirmado el pago, se informa a los demás interesados, como correo, caja y control escolar, sin que el módulo de pagos tenga que conocer directamente cómo trabaja cada uno. | Observer |

###### 2 de septiembre 2026 - Topicos de web y movil