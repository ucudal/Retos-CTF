# Desafío: Frosty Keypad Silver

Para comenzar este desafío, debemos acercarnos y hablar con **Morcel Nougat**, un loco barbudo de dudosa procedencia.  
<br>
![Morcel Nougat](recursos/LobbyFrostyKeyPad.png)

## El reto

Se trata de un teclado que debemos descifrar para acceder a las piezas de un documento que la máquina destrozó en muchos pedazos.  

![LobbyNUM](recursos/Numpad.png)

Morcel menciona que hay un **libro cerca que contiene una pista sobre el código**. Este libro se puede encontrar un poco más a la derecha, detrás de unas cajas. Pero ojo, **no es la única cosa escondida en el mapa**.  

<details>
  <summary><b>Ubicación del libro</b></summary>
  
  ![Sherlock](recursos/Sherlock.png)
</details>

<br>

Al parecer, el libro es una colección de cuentos navideños.  

## Una pista adicional

Además del libro, hay una nota pegada en la máquina. Si interactuamos con ella, veremos una serie de números divididos por dos puntos.  

## Exploración adicional

En un intento inicial, revisé el código fuente del juego para ver si podía encontrar alguna pista adicional. Aunque no encontré nada directamente relacionado con el teclado, descubrí una función que permite activar una linterna. Aunque no estaba relacionado con la tarea principal, mi curiosidad me ganó y decidí probarlo.  

Para activar la linterna, solo bastó con configurar su valor a `true` en la consola insertando el siguiente comando:

```javascript
uvLight.setVisible(true);
```




## Una vez activada, pude ver lo siguiente:  

![Descubrimiento con la linterna2](recursos/Linterna.png)

Aunque esta revelación **no tenía relación directa con el libro**, me llevó a intentar asociar las notas de la máquina con el contenido del libro.

## El descifrado 

Después de revisar el libro, me di cuenta de que la clave seguía el formato: 


<details>
  <summary><b>PÁGINA:PALABRA:LETRA</b></summary>
  El cifrado de libro es una técnica clásica de encriptación que utiliza un texto o libro acordado como clave para codificar mensajes. Cada carácter del mensaje se representa con una referencia a la posición específica dentro del texto clave, indicada como página:palabra:letra. Aunque simple y efectivo si el libro permanece secreto, es un método poco práctico para mensajes extensos y <b>vulnerable</b> si la clave es descubierta.
</details>


<br>

Al aplicar este formato, logré formar la palabra **S-A-N-T-A**. Esto confirmaba que íbamos en la dirección correcta.

## El toque final

Solo faltó que el protagonista sacara su anticuado **Nokia 1100** y comenzara a escribir la palabra dejando así los siguientes dígitos apretados:

```
72682
```

<details>
  <summary><b>Apreta para ver como lo descubrió el protagonista</b></summary>
  
  ![Descubrimiento con la linterna](recursos/FlashLightSuperEdit1100.png)
</details>

<br>

Con esto, ¡logramos descifrar el teclado y completar el desafío! 🎉
