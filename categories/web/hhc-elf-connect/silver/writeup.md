# Elf connect | Silver

### Introducción
Este fue uno de los primeros desafíos a los que nos enfrentamos y, como no teníamos experiencia previa, comenzamos resolviéndolo de forma manual. El juego consistía en clasificar palabras en grupos de 4 relacionadas entre sí. Cada nivel contenía 16 palabras, y nuestro objetivo era formar 4 grupos correctos por nivel.

Al principio, algunas relaciones entre las palabras eran evidentes, lo que hacía que los primeros grupos fueran relativamente fáciles de formar. Sin embargo, a medida que avanzábamos, nos encontramos con palabras mucho más complejas de clasificar, y nuestras ideas para resolver el desafío de manera manual se agotaron.


### Investigación del Código del Juego
En un intento por avanzar, decidimos inspeccionar el código JavaScript del juego directamente desde el navegador. Durante nuestra investigación, descubrimos un script que contenía información clave para resolver el desafío:

Listas de Palabras: El script tenía una estructura que almacenaba todas las palabras de cada nivel. Estas listas coincidían exactamente con las palabras que estábamos clasificando en el juego.

Listas de Posiciones: También identificamos listas de números que, según nuestras suposiciones, representaban las posiciones exactas en las que debíamos seleccionar las palabras para formar los grupos correctos.
En la siguiente imagen se pueden observar estas listas dentro del script que encontramos durante nuestra exploración:


![alt text](image.png)


### Resolución 
Decidimos probar una hipótesis: seguir las posiciones indicadas en la lista numérica y seleccionar las palabras correspondientes. Al hacerlo, logramos formar correctamente los grupos de palabras y avanzar en los niveles.

Sin embargo, este método manual de buscar cada palabra en la lista y luego clasificarla se volvió tedioso, especialmente al intentar avanzar en múltiples niveles. Por esta razón, optamos por automatizar el proceso.

Desarrollamos un programa en Python para simplificar la clasificación de palabras. Este programa tomaba las listas del script y generaba automáticamente las palabras correspondientes a las posiciones indicadas en las listas numéricas. Esto nos permitió resolver los niveles de forma eficiente y sin errores manuales.

El código desarrollado fue el siguiente:


```bash

wordSets = {
    1: ["Tinsel", "Sleigh", "Belafonte", "Bag", "Comet", "Garland", "Jingle Bells", "Mittens", "Vixen", "Gifts",
        "Star", "Crosby", "White Christmas", "Prancer", "Lights", "Blitzen"],
    2: ["Nmap", "burp", "Frida", "OWASP Zap", "Metasploit", "netcat", "Cycript", "Nikto", "Cobalt Strike", "wfuzz",
        "Wireshark", "AppMon", "apktool", "HAVOC", "Nessus", "Empire"],
    3: ["AES", "WEP", "Symmetric", "WPA2", "Caesar", "RSA", "Asymmetric", "TKIP", "One-time Pad", "LEAP", "Blowfish",
        "hash", "hybrid", "Ottendorf", "3DES", "Scytale"],
    4: ["IGMP", "TLS", "Ethernet", "SSL", "HTTP", "IPX", "PPP", "IPSec", "FTP", "SSH", "IP", "IEEE 802.11", "ARP",
        "SMTP", "ICMP", "DNS"]
}

correctSets = [
    [0, 5, 10, 14],  # Set 1
    [1, 3, 7, 9],    # Set 2
    [2, 6, 11, 12],  # Set 3
    [4, 8, 13, 15]   # Set 4
]

for key, words in wordSets.items():
    print(f"Word Set {key}:")
    print("\n".join([f"  Correct Set: {correctSet} -> {[words[i] for i in correctSet]}" for correctSet in correctSets]))

```

## Resultados
Al ejecutar este script, obtuvimos los grupos correctos para cada nivel de forma inmediata. La salida del programa fue la siguiente:

![alt text](image2.png)