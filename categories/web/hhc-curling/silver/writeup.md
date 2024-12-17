## Curling Fun

Se describirá cada paso realizado para resolver el desafío CurlingFun utilizando `curl`. A continuación, se detallan los comandos ejecutados, su propósito y los resultados obtenidos.

### Paso 1: Acceder al puerto HTTP

**Comando:**

```bash
curl --insecure http://curlingfun:8080/
```

Se realiza una solicitud HTTP simple al servidor en el puerto `8080` , para asegurarse de que el servidor responda a solicitudes HTTP no seguras.

### Paso 2: Acceder al puerto HTTPS

**Comando**:

```bash
curl --insecure https://curlingfun:9090/
```

Para confirmar que el servidor HTTPS al puerto `9090` esté activo utilizamos dicho comando, ejecutando la opción `insecure` para saltearse los warnings proveniente de la autofirma.

### Paso 3: Enviar solicitud `POST` al servidor

**Comando**:

```bash
curl --insecure --data "skip=alabaster" https://curlingfun:9090/
```

Mediante la opción  - -data seteamos el parámetro skip.

### Paso 4: Enviamos una cookie

**Comando:**

```bash
curl --insecure --cookie "end=3" https://curlingfun:9090/
```

Se envía una cookie personalizada `end` con el valor 3 con el fin de mantener la sesión o enviar información al servidor.

### Paso 5: Inspeccionar la conexión HTTPS con verbose

**Comando:**

```bash
curl --insecure --verbose https://curlingfun:9090/
```

Utilizando el parámetro - -verbose podemos acceder el modo detallado para visualizar la información completa de la conexión y la respuesta del servidor.

### Paso 6: Enviar un encabezado HTTP

**Comando:**

```bash
curl --insecure --header "Stone: Granite" https://curlingfun:9090/
```

De esta forma se envía un encabezado HTTP personalizado denominado `Stone`  con el valor asignado de `Granite` .

### Paso 7: Acceder a un path especifíco

**Comando:**

```bash
curl --insecure --path-as-is https://curlingfun:9090/../../etc/hacks
```

Accedemos al path [https://curlingfun:9090/../../etc/hacks](https://curlingfun:9090/../../etc/hacks) utilizando el parámetro — path-as-is para que la ruta especifíca no sea modificada automáticamente por curl.

---