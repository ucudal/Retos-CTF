# Santa Vision Part A | Silver Medal

## Introducción

El ejercicio consiste en ir completando distintas partes del desafío para llegar a detener el secuestro del SBN (Santa Broadcast Network), con el cual Alabaster y Wombley se encuentran monopolizando las *feeds*, utilizándola para compartir propaganda y reclutar a elfos.

En esta primera parte tenemos que encontrar el *username* que nos loguea a la SantaVision Portal.

---

## Paso 1: Obtener el IP de nuestra instancia de la infraestructura de SantaVision

Al clickear en el monitor de SantaVision accedemos a la siguiente página:

![Santa Vision inicial](resources/image.png)

Al scrollear por la página, y ver todos sus elementos, se encontró que el único con el que se puede interactuar es el cocodrilo con el gorro navideño que se encuentra abajo a la izquierda. Al clickearlo, se nos abre GateXOR:

![GateXOR status off](resources/image-1.png)

Inicialmente no se observa nada, y parece ser que el *status* de la instancia está en Off. Sabemos que debemos esperar para obtener una IP por la siguiente interacción con el elfo inicial, que nos indica que debemos escanear la IP dada para obtener los servicios que está escuchando:

![Ribb conversación escaneo](resources/image-2.png)

El tiempo de espera puede ser de varios minutos, pero luego de un tiempo se obtiene la IP:

![Mensaje GateXOR](resources/image-4.png)

### Resultado

Obtuvimos la IP de la instancia a escanear.

![IP](resources/image-3.png)

---

## Paso 2: Acceso a la página de Santa Vision Portal

Al intentar acceder a la IP por el navegador, nos encontramos que la IP ha rechazado la conexión:

![Rechaza conexión](resources/image-5.png)

Basándonos en la conversación previa con el elfo Ribb, entendemos que se debe escanear la IP para ver los servicios que están escuchando, encontrando así algún puerto para ingresar.

Para esta tarea se buscó un *scanner* de servicios escuchando, y se hizo uso del más conocido, Nmap:

![Búsqueda nmap](resources/image-6.png)

![Nmap](resources/image-7.png)

Accedemos al sitio de [Nmap](https://nmap.org/man/es/man-version-detection.html), y nos dirigimos a la sección de *Download*:

![Nmap Site](resources/image-8.png)

Seleccionamos la opción para nuestro sistema operativo:

![Nmap Download](resources/image-9.png)

Descargamos el último instalador estable:

![Instalador estable](resources/image-10.png)

Una vez descargado, abrimos el Nmap *setup* y seguimos las siguientes opciones:

![alt text](resources/image-11.png)

![alt text](resources/image-12.png)

![alt text](resources/image-13.png)

Esperamos hasta que la instalación se complete, clickeamos en *Next*:

![alt text](resources/image-14.png)

![alt text](resources/image-15.png)

![alt text](resources/image-16.png)

Clickeamos en *Finish*, abrimos Nmap, apareciéndonos la siguiente GUI:

![Nmap GUI](resources/image-17.png)

En *target* indicamos la IP de nuestra instancia a escanear, y en *profile* seleccionamos *Intense scan, all TCP ports*:

![alt text](resources/image-18.png)

Clickeamos en *Scan* y esperamos a que se complete el escaneo. Puede demorar varios minutos.

![alt text](resources/image-19.png)

Cambiamos de la tab *Host* a *Services* para observar los puertos y servicios escuchando de la IP:

![alt text](resources/image-20.png)

Observamos que hay servicios *http*, *llmnr*, *mqtt*, *ssh*, y *tor-orport* escuchando. Como inicialmente queríamos ver si hay un sitio web para la instancia, vamos a la sección del servicio *http*:

![alt text](resources/image-21.png)

Se obtienen datos del nombre del host, el puerto, protocolo, estado y la versión. Ahora podemos tratar de acceder al sitio desde el navegador usando la IP y el puerto 8000:

![alt text](resources/image-22.png)

![alt text](resources/image-23.png)

Con esto hemos accedido a la página de SantaVision.

---

## Paso 3: Inicio de sesión en la página

Ya se ha llegado al sitio web. Ahora, para completar esta primera parte, debemos obtener el usuario que nos permita loguearnos. Para ello, primero inspeccionamos la página:

![Inspección de página](resources/image-24.png)

Al ver la tab de *Elements*, observamos las *tags*, y algo que nos llamó la atención, un comentario:

![alt text](resources/image-25.png)

Son dos valores que están separados uno de otro, al igual que un usuario y contraseña, por ello decidimos probarlo para iniciar sesión.

![alt text](resources/image-26.png)

### Resultado
![alt text](resources/image-27.png)

---

## Conclusión

Se pudo loguearse en el sitio web, accediendo a un nuevo *path*. Se entrega el *username* usado en el *input* de los objectives:

![alt text](resources/image-28.png)

![alt text](resources/image-29.png)
