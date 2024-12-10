# ACT I: cURLing

<img width="541" alt="Captura de pantalla 2024-12-10 a las 18 36 20" src="https://github.com/user-attachments/assets/ab20786f-ac24-4989-b56c-9ce202bd4b41">


- Básicamente se inició con la lectura de la documentación de cURL para recordar cómo funcionaba, cómo se pasaban los parámetros y otros detalles relacionados con las URLs en cURL.
- Inicialmente procedimos a verificar nuestra ubicación dentro de la terminal. Ejecutando el comando `ls`, se observó que había un archivo llamado `HARD-MODE.txt`.
- Al ejecutar el comando `cat` seguido del nombre del archivo, se abrió el documento, que indicaba realizar el desafío sin guía y proporcionaba una URL con unos parámetros para usar con cURL.
- Al ejecutar el comando con cURL, nos encontramos con una respuesta **301**. Investigando qué significaba esta respuesta, descubrimos que indicaba que el recurso al que intentábamos acceder había sido movido a otro lugar. Inspeccionando el código, se podía ver dentro de la respuesta 301 la nueva URL donde se encontraba el recurso.
- Finalmente, se ejecutó nuevamente el comando cURL, agregando el parámetro `-L` para habilitar el redireccionamiento automático al nuevo lugar, completando así el desafío y obteniendo la recompensa **GOLD**.
- El comando curl utilizado con los parametros fue el siguiente:
  curl -X POST https://curlingfun:9090/ \
     -d "skip=bow" \
     --cookie "end=10" \
     -H "Hack: 12ft"

<img width="404" alt="Captura de pantalla 2024-12-10 a las 18 45 22" src="https://github.com/user-attachments/assets/0da1c5b1-c403-43a9-8861-c3731c205c57">
