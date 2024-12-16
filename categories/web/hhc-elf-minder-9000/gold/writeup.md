# Elf Minder 9000 | Gold

Este desafío planteó un juego de múltiples niveles, con un aumento progresivo de dificultad, hasta llegar a un nivel especial el cuál era imposible superar, lo que nos dió a entender que era necesario generar un pensamiento lateral.

### Exploración inicial

Jugamos varias partidas para comprender la dinámica del juego. Descubrimos que podíamos modificar el camino del personaje en tiempo real, lo que permitió desarrollar estrategias dinámicas para avanzar. Sin embargo, al llegar al último nivel, nos enfrentamos a una pantalla de alta dificultad que no logramos resolver jugando normalmente.

### Análisis del código

Al no encontrar una solución directa, decidimos inspeccionar el código del juego mediante las herramientas de desarrollo del navegador. Identificamos una configuración que utilizaba la propiedad `hidden`, lo que nos permitió habilitar el modo "administrador".

Al explorar las funciones disponibles en `game.` desde la consola, descubrimos que podíamos manipular entidades del mapa, como piedras, cajas o túneles. Intentamos eliminar obstáculos, pero el juego tenía validaciones que impedían la eliminación de elementos esenciales.

### Modificación del mapa

En lugar de eliminar elementos, optamos por agregar nuevas entidades estratégicamente. Utilizamos las posiciones exactas extraídas del código para cumplir con los requisitos del nivel. 

Confirmamos que era necesario modificar el código ya que las inserciones realizadas a través de este medio eran imposible de realizar dentro de la interfaz gráfica.

Esto nos permitió avanzar en el juego y superar este desafío.