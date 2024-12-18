# Act 2 | Hardware Hacking Parte 2 | Gold

## Introducción

Esta vez, el objetivo es modificar directamente la base de datos para actualizar la **tarjeta 42**. Aunque este detalle no es evidente al principio, el elfo provee pistas importantes mencionando la necesidad de trabajar con una HMAC (Hash-based Message Authentication Code).

Este escenario combina la manipulación de datos en un sistema restringido con el entendimiento y la correcta implementación de mecanismos de seguridad como el HMAC, utilizado para garantizar la integridad de los datos. 

### Paso 1: Exploración Inicial

En el sistema, encontramos un único archivo llamado access_cards, identificado como una base de datos SQLite 3.x:

```bash

slh@slhconsole> ls
access_cards
slh@slhconsole> file access_cards
access_cards: SQLite 3.x database, last written using SQLite version 3040001, file counter 4, database pages 32, cookie 0x2, schema 4, UTF-8, version-valid-for 4
```

Podemos interactuar con la base de datos directamente utilizando el cliente `sqlite3`:

```bash
sqlite3 access_cards
SQLite version 3.40.1 2022-12-28 14:03:47
```

### Paso 2: Inspección de la Estructura de la Base de Datos

Usamos el comando `.schema` para inspeccionar la estructura de la tabla access_cards:

```sql

.schema access_cards
CREATE TABLE access_cards (
            id INTEGER PRIMARY KEY,
            uuid TEXT,
            access INTEGER,
            sig TEXT)
```

La tabla contiene cuatro columnas:

- **id**: Número de la tarjeta.
- **uuid**: Identificador único de la tarjeta.
- **access**: Indicador de acceso (0 = Denegado, 1 = Permitido).
- **sig**: HMAC de la entrada.

### Paso 3: Revisión de la Entrada para la Tarjeta 42

Consultamos la entrada correspondiente a la tarjeta **42**:

```sql
SELECT * FROM access_cards WHERE id=42;

42|c06018b6-5e80-4395-ab71-ae5124560189|0|ecb9de15a057305e5887502d46d434c9394f5ed7ef1a51d2930ad786b02f6ffd
```

Observamos que la tarjeta tiene acceso denegado (access = 0) y un HMAC asociado en la columna sig.

### Paso 4: Actualización de la Entrada

Modificamos el valor de **access** a `1` para otorgar acceso a la tarjeta:

```sql
UPDATE access_cards SET access=1 WHERE id = 42;
```

Sin embargo, el valor de sig ya no es válido, ya que no corresponde a los datos actualizados. Necesitamos generar un nuevo HMAC.

### Paso 5: Exploración de la Configuración

Inspeccionamos las tablas disponibles en la base de datos y encontramos una tabla adicional llamada **config**:

```sql
.tables
access_cards  config

SELECT * FROM config;

1|hmac_secret|9ed1515819dec61fd361d5fdabb57f41ecce1a5fe1fe263b98c0d6943b9b232e
2|hmac_message_format|{access}{uuid}
3|admin_password|3a40ae3f3fd57b2a4513cca783609589dbe51ce5e69739a33141c5717c20c9c1
4|app_version|1.0
```

Los datos relevantes son:

1. hmac_secret: La clave HMAC necesaria para la generación.
    - Valor: `9ed1515819dec61fd361d5fdabb57f41ecce1a5fe1fe263b98c0d6943b9b232e`
2. hmac_message_format: El formato de los datos para el HMAC.
    - Valor: `{access}{uuid}`

### Paso 6: Generación del Nuevo HMAC

Para generar el nuevo HMAC:

1. Formateamos el mensaje combinando los datos:
    - access = 1
    - uuid = c06018b6-5e80-4395-ab71-ae5124560189
    - Mensaje: `1c06018b6-5e80-4395-ab71-ae5124560189`
2. Utilizamos Cyberchef para generar el HMAC:
    - Pegamos el mensaje en el campo Input.
    - Pegamos la clave (`hmac_secret`) en el campo Key.
    - Seleccionamos el algoritmo HMAC con SHA-256.

### Paso 7: Actualización Final en la Base de Datos

Finalmente, actualizamos el campo **sig** de la tarjeta 42 con el nuevo HMAC generado:

```sql
UPDATE access_cards SET sig='135a32d5026c5628b1753e6c67015c0f04e26051ef7391c2552de2816b1b7096' WHERE id=42;
```

Resultado:

![image.png](resources/image.png)
