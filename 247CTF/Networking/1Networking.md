# ERROR REPORTING PROTOCOL
## CATEGORÍA: NETWORKING

### PRESENTACIÓN DEL PROBLEMA:
Al entrar a este ejercicio, nos encontramos con esta consigna:
"Can you identify the flag hidden within the error messages of this ICMP traffic?"
Este reto nos proporciona un archivo comprimido, que al descargarlo y descomprimirlo encontramos un archivo .pcap con tráfico de red capturado bajo el protocolo ICMP, y el título sugería que los datos importantes estaban relacionados con un "protocolo de reporte de errores". La idea de este ejercicio es encontrar una flag oculta dentro de ese tráfico, para asi resolverlo.


### PASO A PASO DEL PROCESO:

**INTENTO 1** 

Abrí el archivo con Wireshark para hacer una revisión inicial. Noté que todo el tráfico estaba compuesto por paquetes ICMP tipo echo reply. Revisando uno por uno, vi que cada uno contenía datos binarios (48 bytes) en el campo Data. Intenté interpretar directamente esos valores como texto, pero no mostraban nada legible más allá de un fragmento con el texto "send the flag:".

**INTENTO 2** 

Sospechando que los datos podían estar codificados de alguna manera, usé tshark para extraer todos los campos data de los paquetes ICMP del .pcap:

tshark -r error_reporting.pcap -Y "icmp" -T fields -e data > datos_icmp.txt

**INTENTO 3**

Convertí la cadena hexadecimal a binario usando Python. El resultado fue una gran cantidad de bytes no legibles, pero al inspeccionar el contenido noté que empezaba con ffd8ffe0, que corresponde a la cabecera de un archivo JPEG. Ahí entendí que lo que estaba reconstruyendo era una imagen.

Guardé los datos como archivo .jpg con este código en python:

with open("output.jpg", "wb") as f:
    f.write(bytes.fromhex(hexdata))
Abrí la imagen y ahí estaba: la flag aparecía claramente en texto blanco sobre fondo oscuro.

 **DESCRIPCIÓN DE LA SOLUCIÓN:** 

Los datos ICMP contenían una imagen fragmentada en bloques de 48 bytes. Extraje todos esos fragmentos, los uní y reconstruí la imagen completa. La flag estaba oculta visualmente en esa imagen, y se revelaba al abrirla como un archivo .jpg.

### FLAG:
247CTF{580e6d627470448064fa7bffd6284ddf}



**Autor/a: Juan Sosa Dias**