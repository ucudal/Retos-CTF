# Santa Vision Part C | Silver Medal

## Introducción

En esta tercera parte debemos suscribirnos al MQTT topic de frostbitfeed, usando los datos que se nos dan en la plataforma de Santa Vision, indicando cuál es el código de la operación secreta de los elfos.

---

## Paso 1: Conectarse al host y puerto de MQTT

Sabemos que las conexiones a las feeds se hacen por medio de MQTT, como lo hemos visto en las anteriores partes del desafío. Esto no solo está hardcodeado al inspeccionar el JS de la página, sino que también al escanear por servicios escuchando en el host, nos aparece el servicio de MQTT, y obtenemos el puerto en el que está escuchando:

![alt text](resources/image-11.png)

Debemos suscribirnos a la feed de frostbitfeed, para esto buscamos una GUI que nos permitiera suscribirnos de una forma visualmente más amigable:

![alt text](resources/image.png)

Ingresamos a la página de MQTTX:

![alt text](resources/image-1.png)

Clickeamos en download:

![alt text](resources/image-2.png)

Seleccionamos nuestro sistema operativo y descargamos el instalador en la sección Desktop:

![alt text](resources/image-3.png)

Clickeamos el instalador, e indicamos si deseamos instalar MQTTX solo para nuestro usuario o para todos los del equipo:

![alt text](resources/image-4.png)

Presionamos Next, e indicamos dónde deseamos instalar MQTTX. Recomendamos dejar el default:

![alt text](resources/image-5.png)

Clickeamos Next, y esperamos a que se termine la instalación:

![alt text](resources/image-6.png)

Luego de terminada la instalación, dejamos la checkbox de ejecutar MQTTX para ya usar el programa, presionamos terminar:

![alt text](resources/image-7.png)

Accedemos a la interfaz de MQTTX, y clickeamos en el signo de "+" arriba, a la izquierda de "Connections":

![alt text](resources/image-8.png)

Seleccionamos la opción de New Connection:

![alt text](resources/image-9.png)

Ingresamos el Name que deseemos, en el host ingresamos la IP de nuestra instancia de SantaVision, y el puerto lo dejamos en el default:

![alt text](resources/image-10.png)

Nota: Sabemos que el puerto default es el que debemos usar porque en el nmap el servicio de MQTT está escuchando en ese puerto

Para el usuario y contraseña primero se probó ingresar el elfmonitor, y SiteElfMonitorRole, como en la página web:

![alt text](resources/image-13.png)

### Resultado

Presionamos Connect arriba a la izquierda, y deberíamos obtener el siguiente resultado:

![alt text](resources/image-12.png)

---

## Paso 2: Suscribirse a la feed de frostbitfeed

Una vez conectados, presionamos en + New Subscription para suscribirnos a la feed:

![alt text](resources/image-14.png)

Ponemos en el topic la "frostbitfeed":

![alt text](resources/image-15.png)

La suscripción sirvió, y deberíamos poder conectarnos a la frostbitfeed, apareciéndonos a la derecha todos los mensajes que fueron publicados y/o recibidos en la feed:

![alt text](resources/image-16.png)

### Resultado

Luego de esperar unos minutos, observamos que los mensajes se empiezan a repetir, y que nunca se menciona el nombre de una operación:

![alt text](resources/image-17.png)

Pero sí nos aparece un mensaje que indica que hay mensajes adicionales en la SantaFeed:

![alt text](resources/image-18.png)

Y sabemos que este es un dato relevante ya que en el objetivo se nos pregunta si hay otras feeds a las que se puede uno conectar:

![alt text](resources/image-19.png)

---

## Paso 3: Suscribirse a la santafeed

Nuevamente hacemos una new subscription, pero esta vez al topic de santafeed:

![alt text](resources/image-20.png)

Nos conectamos a la feed, y hacemos click en la suscripción de santafeed para que solo nos aparezcan los mensajes de dicho topic:

![alt text](resources/image-21.png)

Al leer los mensajes por un minuto, vemos que se menciona una operación con el nombre Idemcerybu:

![alt text](resources/image-22.png)

### Resultado

Consideramos que este puede ser el nombre de la operación, vamos al objetivo, e ingresamos el dato:

![alt text](resources/image-23.png)

Obtenemos la silver medal:

![alt text](resources/image-24.png)
