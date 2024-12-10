# Introducción a CTF
### Índice
- [¿Qué es un CTF?](#qué-es-un-ctf)
- [Conocimientos básicos para empezar en CTF](#conocimientos-básicos-para-empezar-en-ctf)
- [Recursos para aprender conceptos básicos](#recursos-para-aprender-conceptos-básicos)

## ¿Qué es un CTF?
### Definición
Un CTF (Capture The Flag) es un tipo de juego, en formato de competición online o evento, diseñado para poner a prueba, entrenar y mejorar tus habilidades de hacking. En estas competencias, los participantes enfrentan una serie de desafíos relacionados con la seguridad informática, cuyo objetivo principal es encontrar una "bandera" o "flag".

Estas banderas suelen ser cadenas de texto o archivos que demuestran que se ha superado con éxito un desafío en particular. Cuando resuelves un reto y obtienes la bandera, generalmente ganas puntos. La cantidad de puntos depende de la dificultad del desafío, el tamaño del equipo y el tiempo que tardes en resolverlo.

### Tipos de CTF
- **Jeopardy-style CTF**:

    Se basa en resolver desafíos agrupados en categorías, como por ejemplo:
    - **Criptografía**: resolver acertijos cifrados.
    - **Web**: explorar y explotar vulnerabilidades de aplicaciones en web.
    - **Mobile**: investigar y analizar aplicaciones móviles, descubriendo. vulnerabilidades en APKs, permisos indebidos o fugas de información.

- **Attack-Defense CTF**:
    
    En estos, los equipos compiten en una red simulada donde deben:
    - Defender sus propios sistemasde los atacantes de otros equipos.
    - Explorar y atacar los sistemas rivales para capturar sus banderas.
    
    Este fromato simula situaciones reales de ciberseguridad, como pentesting y gestión de incidentes.

- **Mixed-style CTF**:

    Combina elementos de los dos anteriores. Los equipos resuelven retos tipo Joepardy para ganar puntos y pueden usar esos puntos para mejorar su defensa o lanzar ataques contra otros equipos, creando una dinámica estratégica. 

## Conocimientos básicos para empezar en CTF

Antes de empezar en el mundo de los CTFs, es importante tener como base algunos conceptos fundamentales de las tecnologías que comunmente son utilizadas.

### Desarrollo Web
- **HTML, CSS y JavaScript**: comprender cómo funcionan los sitios web.
- **HTTP y peticiones web**:
    - Métodos HTTP (GET, POST, PUT, DELETE).
    - Encabezados HTTP y cookies.
- **Familiaridad con vulnerabilidades web**:
    - SQL Injection.
    - Cross-Site Scripting (XSS).
    - Directory Traversal.
- **Herramientas**:
    - Burp Suite (edición comunitaria).
    - Postman para interactuar con APIs.

### Programación
- **Lenguajes comunes**:
    - Python
    - JavaScript
    - Bash
- **Habilidades esenciales**:
    - Lectura y análisis de código.
    - Debugging con herramientas como IDEs.

### Sistemas operativos
- **Linux**
    - Navegación por el sistema de archivos usando la terminal.
    - Comandos básicos: `ls`, `cat`, `chmod`.
    - Uso de herramientas como curl.
- **Windows**
    - Conocimiento básico del registro de Windows y PowerShell.
    - Adminisración de permisos.

## Recursos para aprender conceptos básicos
- [PortSwigger Web Security Academy](https://portswigger.net/web-security):  
    Un recurso especializado en vulnerabilidades web, con laboratorios para practicar temas como SQLi, XSS y CSRF.

- [Postman Academy](https://academy.postman.com/):  
    Un recurso para comprender el funcionamiento de las APIs, aprender a crear y enviar peticiones HTTP, y analizar sus respuestas.

- etc...