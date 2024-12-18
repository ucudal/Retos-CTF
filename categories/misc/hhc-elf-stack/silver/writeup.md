# Elf Stack Silver

## Introducción

En este desafío, se nos entregaron varios archivos con registros o logs, los cuales debían ser analizados utilizando herramientas y comandos de la línea de comandos de Linux, como cat, grep, curl, sort y uniq, entre otros. El propósito principal era extraer información relevante de estos archivos mediante la combinación de diferentes comandos y opciones.

Los logs son registros detallados de eventos generados por sistemas, aplicaciones o servidores que almacenan información crítica, como el acceso de usuarios, URLs visitadas, códigos de respuesta, direcciones IP y fechas de los eventos.

El desafío constaba de diferentes niveles de dificultad, con preguntas que iban desde simples consultas hasta análisis más complejos de los registros. 

A continuación, se detalla cada comando utilizado para resolver las preguntas del desafío

## Desarrollo

1. cat *.log | cut -d " " -f 4 | sort | uniq  respuesta: 5
2. cat *.log | cut -d " " -f 4 | sort | uniq -c  respuesta: AuthLog
3. grep AuthLog *.log | more respesta: hostname

![image.png](resources/image.png)

4. cat *.log | cut -d " " -f 4 | sort | uniq -c   respuesta: NetflowPmacct

![image.png](resources/image 1.png)

5. grep NetflowPmacct *.log | head -n 1  respuesta: port_dst

![image.png](resources/image 2.png)

6. cat *.log | cut -d " " -f 4 | sort | uniq -c  respuesta: SnowGlowMailPxy

![image.png](resources/image 3.png)

7. grep SnowGlowMailPxy *.log | head -n 1  respuesta: body

![image.png](resources/image 4.png)

8. grep GreenCoat *.log | cut -d " " -f 3 | uniq  respuesta: SecureElfGwy

![image.png](resources/image 5.png)

9. grep GreenCoat *.log | head -n 1     respuesta: url

![image.png](resources/image 6.png)

10. grep GreenCoat *.log | grep -Po 'url": "\K[^"]*' | sort | uniq -c | sort -n

![image.png](resources/image 7.png)

11. grep WindowsEvent *.log | ggrep -Po '"Channel": "\K[^"]*' | sort | uniq -c | sort -h  respuesta: 5

![image.png](resources/image 8.png)

12. grep WindowsEvent *.log | ggrep -Po '"Channel": "\K[^"]*' | sort | uniq -c | sort -h   respuesta: Microsoft-Windows-Sysmon/Operational

![image.png](resources/image 9.png)

13. Respuesta: 6 

![image.png](resources/image 10.png)

14. Respuesta: 4697

![image.png](resources/image 11.png)

15. grep WindowsEvent *.log |  grep -o 'Subject_AccountName=[^ ]**' | sort | uniq | wc -l 

respuesta: 0

![image.png](resources/image 12.png)


### ¿Cómo funciona cada comando?

`cat *.log`

Se utiliza para leer y concatenar, en este caso, todos los archivos .log.

`cut -d " " -f 4` 

Este comando extrae partes especificas del texto, utilizando -d como delimitador (en este caso “ ”), y la operación -f para seleccionar un campo de cada línea (en este caso el campo 4) .

`sort`

Utilizado para ordenar las líneas del texto, ya sea númericamente como alfabéticamente.

`uniq`

Elimina las líneas duplicadas de forma consecutiva, por ello, si se busca eliminar aquellas palabras que se repiten es importante antes realizar una operación de ordenamiento.

`uniq -c`

Al utilizar el parámetro `-c` se retorna las ocurrencias de cada palabra única sin duplicados consecutivos.

`grep AuthLog *.log | more` 

La operación `grep`  se utiliza con el fin  de obtener líneas que coincidan con un patrón dado (en este caso que contengan el texto `AuthLog`). La opción `more` se usa para que la salida se visualice de forma más cómoda.

`head -n 1`

La operación `head`  la utilizamos para mostrar las primeras líneas del archivo, y el uso del parámetro `-n 1` es para indicar que solo retorne la primera línea.