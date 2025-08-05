import random
from secret import flag

rounds = 5                      # se hace 5 veces
block_size = 8               # 8 bits por bloque
sa = {
    0: 15, 
    1: 2, 
    2: 14, 
    3: 0, 
    4: 1, 
    5: 3, 
    6: 10, 
    7: 6, 
    8: 4, 
    9: 11, 
    10: 9, 
    11: 7, 
    12: 13, 
    13: 12, 
    14: 8, 
    15: 5
}
sb = {
    0: 12, 
    1: 8, 
    2: 13, 
    3: 6, 
    4: 9, 
    5: 1, 
    6: 11, 
    7: 14, 
    8: 5, 
    9: 10, 
    10: 3, 
    11: 4, 
    12: 0, 
    13: 15, 
    14: 7, 
    15: 2
}

key = [random.randrange(255), random.randrange(255)] * 4    # aca solo se sacan dos numeros a lazar y se multiplica por 4, ej: [4 12 4 12 4 12 4 12]
to_bin = lambda x, n=block_size: format(x, "b").zfill(n)    # convierte a binario y completa con ceros a la izquierda
to_int = lambda x: int(x, 2)                                # convierte de binario a entero
to_chr = lambda x: "".join([chr(i) for i in x])       # convierte de entero a caracteres
to_ord = lambda x: [ord(i) for i in x]      # convierte de caracteres a enteros
bin_join = lambda x, n=int(block_size / 2): (str(x[0]).zfill(n) + str(x[1]).zfill(n))       # une dos cadenas binarias con ceros a la izquierda
bin_split = lambda x: (x[0 : int(block_size / 2)], x[int(block_size / 2) :])  # divide una cadena binaria en dos partes
str_split = lambda x: [x[i : i + block_size] for i in range(0, len(x), block_size)]            # divide una cadena en bloques de tamaño block_size (osea 8)
xor = lambda x, y: x ^ y                     # realiza una operacion XOR entre dos numeros

def sustituir(a, b):                    # realiza la sustitucion S-box, esto es, reemplaza los valores de a y b con los valores de las S-box
    return sa[a], sb[b]

def permutacion(a):             # realiza la permutacion P-box, esto es, reordena los bits de a
    return a[5] + a[2] + a[3] + a[1] + a[6] + a[0] + a[7] + a[4]

def generar_claves(k):    # esto lo que hace es generar las claves de ronda, que son 5 claves de 8 bits cada una
    return [
        k[i : i + int(block_size)] + k[0 : (i + block_size) - len(k)]
        for i in range(rounds)
    ]

def xor_estado_clave(state, k):         # esta funcion realiza la operacion de clave de ronda, que es una operacion XOR entre el estado y la clave de ronda
    return [xor(state[i], k[i]) for i in range(len(state))]

def aplico_Sbox_Pbox(e):                  # esta funcion realiza el proceso de encriptacion, que es la aplicacion de la S-box y P-box
    encrypted = []                           # arranca vacio
    for i in e:
        a, b = bin_split(to_bin(ord(i)))     # divide el caracter en dos partes de 4 bits cada una
        sa, sb = sustituir(to_int(a), to_int(b))  # aplica la S-box a cada parte
        pe = permutacion(
            bin_join((to_bin(sa, int(block_size / 2)), to_bin(sb, int(block_size / 2))))  # une las partes y aplica la P-box
        )
        encrypted.append(to_int(pe)) # convierte el resultado a entero y lo agrega a la lista
    return encrypted

def encriptttttttttttttttttador(p, k):
    keys = generar_claves(k)
    bloque_bandera = str_split(p)    # divido el mensaje en bloques de 8 bits
    for b in range(len(bloque_bandera)):     # de 1 a 8
        for i in range(rounds):     # 5 veces
            xor_bloque_bandera = xor_estado_clave(to_ord(bloque_bandera[b]), keys[i])
            bloque_bandera[b] = to_chr(aplico_Sbox_Pbox(to_chr(xor_bloque_bandera)))
    print(bloque_bandera)
    return [ord(e) for es in bloque_bandera for e in es]

encrypted = encriptttttttttttttttttador(flag, key)
print("Encrypted flag => %s" % encrypted)

encrypted_flag = [190, 245, 36, 15, 132, 103, 116, 14, 59, 38, 28, 203, 158, 245, 222, 157, 36, 100, 240, 206, 36, 205, 51, 206, 90, 212, 222, 245, 83, 14, 222, 206, 163, 38, 59, 157, 83, 203, 28, 27]

inv_sa = {
    15: 0, 
    2: 1, 
    14: 2, 
    0: 3, 
    1: 4, 
    3: 5, 
    10: 6, 
    6: 7, 
    4: 8, 
    11: 9, 
    9: 10, 
    7: 11, 
    13: 12, 
    12: 13, 
    8: 14, 
    5: 15
}

inv_sb = {
    12: 0, 
    8: 1, 
    13: 2, 
    6: 3, 
    9: 4, 
    1: 5, 
    11: 6, 
    14: 7, 
    5: 8, 
    10: 9, 
    3: 10, 
    4: 11, 
    0: 12, 
    15: 13, 
    7: 14, 
    2: 15
}

def inversa_sustituir(a, b):     
    return inv_sa[a], inv_sb[b]

def inversa_permutacion(a):      
    return a[5] + a[3] + a[1] + a[2] + a[7] + a[0] + a[4] + a[6]

def aplico_Sbox_Pbox_invertida(lista_enteros, clave):      # me hace lo mismo pero en el orden al revez q hoy
    resultado = []
    contador = 0
    for i in lista_enteros:
        binario = to_bin(i)
        perm_deshecha = inversa_permutacion(binario) # paso a binario y hago la permutacion al reve
        a, b = bin_split(perm_deshecha) # aca divido en 2 y aplico las cajas
        inv_a, inv_b = inversa_sustituir(to_int(a), to_int(b))

        unidos = bin_join((to_bin(inv_a, int(block_size / 2)), to_bin(inv_b, int(block_size / 2)))) #uno y paso a entero
        numero = to_int(unidos)

        if contador % 2 == 0:
            val = xor(numero, clave[0])     # esto es lo mismo, pero no tengo la clave, aun
        else:
            val = xor(numero, clave[1])
        contador += 1

        resultado.append(val)
    return resultado

def desencriptador(codigo_encriptado, clave):
    claves = generar_claves(clave)    # se generan las 5 claves
    bloques = str_split(codigo_encriptado)    # se divide la lista en bloques de 8

    for b in range(len(bloques)):
        bloque = bloques[b]
        for i in reversed(range(rounds)):  # se desencripta en orden inverso (última clave a primera)
            bloque = aplico_Sbox_Pbox_invertida(bloque, claves[i])
        bloques[b] = bloque
    return [chr(e) for bloque in bloques for e in bloque]

for i in range(256):
    for j in range(256):
        clave = [i, j] * 4
        bandera_descifrada = desencriptador(encrypted_flag, clave)
        bandera = ''.join(bandera_descifrada)
        if '247CTF' in bandera:
            print("Bandera: "+bandera)
            break
    else:
        continue
    break