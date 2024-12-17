## Elf Minder 9000 - Gold
El problema de Elf Minder 9000 gold, es resolver el ultimo desafio llamado A Real Pickle. El cual se resuelve de forma distinta a los otros desafios, a principio parece que no tiene solución sin editar los obstáculos.

### Paso 1: Exploración Inicial
Primero se realizó un reconocimiento del juego, identificando sus mecánicas básicas y la dificultad progresiva de los niveles. Se descubrió que el último nivel era prácticamente imposible de completar mediante el juego normal.

Buscando en el codigo de source, se encuentra esto:

```
<div class="admin-controls hidden">
  <! - <button id="startBtn">Start</button> →
  <button id="resetBtn">Reset</button>
  <button id="clearPathBtn">Clear Path</button>
  <button id="clearEntitiesBtn">Clear Entities</button>
  <fieldset id="tools">…</fieldset>
</div>
```

### Paso 2: 

Al remover el hidden, se pueden ver opciones para editar el escenario:

<img width="642" alt="image" src="https://github.com/user-attachments/assets/a3943b32-b879-4b96-8ca3-63ae07ecf3fb" />

### Paso 3:

Si tocamos en "Clear Entities" el mapa se vacia totalmente:

<img width="656" alt="image" src="https://github.com/user-attachments/assets/55de858b-3960-4c4f-a85c-f3f5888275a6" />

### Paso 4:

Intentamos resolverlo:

<img width="649" alt="image" src="https://github.com/user-attachments/assets/b82150f6-4f28-4560-98f2-f70c03d89885" />

El juego nos lanza un error, por lo cual la solución no es simplemente eliminar los obstáculos.

### Paso 5

Gracias a esta parte del Source code podemos identificar el uso de los springs como portales hacia el inicio, utilizando asi los objetos a nuestro favor para llegar al destino.

<img width="571" alt="image" src="https://github.com/user-attachments/assets/c20c874a-3623-4b73-bec3-488aa7fcb050" />

### Paso 6:

Intentamos usando los objetos que nos da el desafío y se puede solucionar.

<img width="641" alt="image" src="https://github.com/user-attachments/assets/9c7c37fa-ba31-4557-bb26-be274a046138" />



