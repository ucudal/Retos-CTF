THE TEXT EDITOR JAIL
MISCELLANEOUS

![imagen](<Captura de pantalla 2025-08-04 184454.png>)

En este ejercicio se nos presenta una consola interactiva, desde la cual podemos ejecutar comandos en un entorno controlado. La tarea consiste en descubrir la flag, utilizando únicamente comandos disponibles dentro de esa consola.
El primer paso fue intentar listar los archivos presentes en el entorno. Utilizamos :!ls para hacer esto.
Este comando nos mostró los archivos disponibles en el directorio actual. El único archivo que existe es run_for_flag.
Luego intentamos ejecutar este archivo con :!./run_for_flag
Y este al ser ejecutado nos muestra la flag que estamos buscando.

Flag: 247CTF{c69287be15653ac9ab47dcd3f2fcd8fa}
