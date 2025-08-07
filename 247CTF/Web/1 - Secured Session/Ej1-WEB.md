# SECURED SESSION  
## CATEGORÍA: Web Exploitation  

### PRESENTACIÓN DEL PROBLEMA:  
En este desafío, el objetivo era obtener la bandera ubicada en la ruta `/flag` de un sitio web. Para lograrlo, se utilizó **Burp Suite** para interceptar y analizar la petición, y luego se decodificó el valor de `sessionID` en múltiples pasos para revelar la flag.  
 

### PASO A PASO DEL PROCESO:  

**INTENTO 1**  
- Comenzamos el reto explorando el sitio web y revisando el código para identificar rutas relevantes.  
- Detectamos que existía una ruta `/flag` que parecía ser la clave para obtener la bandera.  

**INTENTO 2**  
- Usamos **Burp Suite** en modo proxy para interceptar la petición hacia `/flag`.  
- En **Proxy > HTTP history**, localizamos la request correspondiente.  
- Revisamos la **response** y encontramos un parámetro llamado `sessionID`.  

**INTENTO 3**  
- Copiamos el `sessionID` y lo pegamos en el **Decoder** de Burp Suite.  
- Seleccionamos la opción **Decode as... → Base64**.  
- El resultado fue otro texto codificado, por lo que repetimos el proceso de decodificación en Base64.  
- Después de la segunda decodificación, obtuvimos un texto entre comillas.  

**INTENTO 4**  
- Pegamos ese texto nuevamente en el Decoder y, finalmente, obtuvimos la bandera en claro.  

**DESCRIPCIÓN DE LA SOLUCIÓN:**  
La solución consistió en interceptar la respuesta del servidor en la ruta `/flag`, copiar el valor de `sessionID` y decodificarlo dos veces en Base64. Luego, el texto resultante se volvió a decodificar para revelar la bandera final. El proceso se realizó íntegramente con **Burp Suite**.  

### FLAG:  
`247CTF{FLAG_DE_EJEMPLO}`  

**Autor/a:** Diego Zucca  
