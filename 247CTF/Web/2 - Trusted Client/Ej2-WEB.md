# TRUSTED CLIENT  
## CATEGORÍA: Web Exploitation  

### PRESENTACIÓN DEL PROBLEMA:  
En este desafío, el objetivo era analizar el código JavaScript del formulario de login, decodificarlo utilizando un **JSFuck Decoder** y extraer la bandera oculta.  


### PASO A PASO DEL PROCESO:  

**INTENTO 1**  
- Comenzamos el reto inspeccionando la página del login.  
- Hicimos clic derecho → **Inspeccionar** (o usamos `F12`) para abrir las herramientas de desarrollo.  
- Fuimos a la pestaña **Elements** para revisar el HTML.  

**INTENTO 2**  
- Buscamos un bloque `<script>` que contenía la lógica de validación.  
- Dentro del código, localizamos la función **`onSubmit`**.  
- Copiamos todo su contenido.  

**INTENTO 3**  
- Abrimos [JSFuck Decoder](https://enkhee-osiris.github.io/Decoder-JSFuck/).  
- Pegamos el contenido de la función en el recuadro del decoder.  
- Seleccionamos **versión 5** para decodificar.  
- Si no funcionaba, probábamos con **versión 4**.  

**INTENTO 4**  
- Esperamos a que la decodificación finalizara.  
- El resultado mostró una **función anónima** con la lógica original.  
- Dentro de esa función, encontramos la **password** en texto plano.  

**DESCRIPCIÓN DE LA SOLUCIÓN:**  
La solución consistió en inspeccionar el HTML de la página para ubicar la función `onSubmit`, copiar su contenido y decodificarlo con la herramienta JSFuck Decoder. Al completar la decodificación, la función resultante reveló la contraseña, que correspondía directamente a la bandera del reto.  

### FLAG:  
`247CTF{FLAG_DE_EJEMPLO}`  

**Autor/a:** Diego Zucca  
