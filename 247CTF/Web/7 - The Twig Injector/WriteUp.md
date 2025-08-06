# THE TWIG INJECTOR
## CATEGORÍA: WEB

### PRESENTACIÓN DEL PROBLEMA:
"Can you abuse the Twig injector service to gain access to the flag hidden in the $_SERVER array?"

Analisis del problema: Accedo a una página con una ruta /inject que recibe un parámetro vulnerable a inyección Twig. El objetivo es mostrar la flag escondida en el servidor, dentro del arreglo SERVER. El problema es que hay un filtro que no me deja usar muchos caracteres, como $, mayúsculas, números o corchetes.

### CAPTURA DE PANTALLA DEL PROBLEMA PRESENTADO 

Nos muestra este codigo en un URL

![imagen](Imagenes\twig1.png)

### PASO A PASO DE INTENTOS DE SOLUCIÓN:

**INTENTO 1** 

1.1. Entro al link del reto y veo que hay una ruta /inject.

1.2. Abro la consola del navegador y reviso el contenido. Todo lo que mando como parámetro inject se muestra reflejado en pantalla.

1.3. Pruebo con texto plano en la URL:
https://03a34e9cc152013a.247ctf.com/inject?inject=hola
Se muestra en pantalla, así que el contenido se está interpretando dentro del template Twig.

![imagen](Imagenes\twig2.png)

1.4. Veo que hay una inyección Twig, pero también noto que hay un filtro que limpia caracteres como $, números, mayúsculas, paréntesis, etc.

1.5. Intento acceder directamente al arreglo server con algo como {{ _SERVER }} pero no funciona, porque el $ está bloqueado y los corchetes también.

1.6. Pruebo escribir expresiones básicas de Twig, como {{ 4+4 }} pero eso también parece filtrado o se muestra como texto plano.

Resultado: No logro acceder a información útil ni ejecutar expresiones Twig complejas. Confirmo que hay inyección, pero estoy muy limitado por el filtro de caracteres.



**INTENTO 2** 

2.1. Reviso qué caracteres están permitidos por el filtro /[^{\.}a-z\|\_]/. Solo se permiten letras minúsculas, llaves, puntos, | y guion bajo.

2.2. Pienso que app.request.server es un objeto accesible dentro del contexto de Twig. Intento accederlo directamente.

2.3. Armo la URL: https://656666ed28cda34b.247ctf.com/inject?inject={{app.request.server}}


![imagen](Imagenes\twig3.png)

2.4. Al probarla en el navegador, me devuelve un error 500 Internal Server Error.

2.5. Esto confirma que Twig no puede renderizar un objeto complejo como app.request.server directamente sin aplicar un filtro que lo convierta en string.

Resultado: El intento falla. No logro obtener información útil ni acceder a la flag.

**INTENTO 3** 

3.1. Me acuerdo que Twig tiene filtros como join y json_encode, que permiten transformar un array en texto plano.

3.2. Como ya vi que app.request.server es equivalente a $_SERVER, intento convertir ese array en texto con el filtro join.

3.3. Escribo directamente en la URL: https://03a34e9cc152013a.247ctf.com/inject?inject={{app.request.server|join}}

3.4. Se renderiza una larga cadena de texto. No se ve muy claro al principio, pero busco manualmente si aparece algo como 247CTF{...}.

3.5. Encuentro la flag escondida dentro del contenido que se imprime en pantalla, mezclada entre otras variables del servidor.

![imagen](Imagenes\twig4.png)

Resultado: Con {{app.request.server|join}} consigo imprimir todo el contenido del array del servidor como un string plano. Ahí adentro aparece la flag.


 **DESCRIPCIÓN DE LA SOLUCIÓN:** 

Aprovecho que el filtro join está permitido, lo aplico a app.request.server para convertir el array en texto plano.

Twig evalúa la expresión y devuelve todo el contenido como un string.

Busco la flag dentro del resultado y la encuentro camuflada entre los datos del servidor.

### FLAG:
Flag Capturada: 247CTF{b8d4dce713400424bc2ab7fa673f231c}



**Autor/a: Nombre Apellido**
Diego Renaldin 