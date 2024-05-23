# -*- coding: UTF-8 -*-
"""
Encriptacion Cifrado Cesar
"""
ALFABETO = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def cifrado_cesar(mensaje, clave):
    """
    Funcion para cifrar un mensaje
    Args:
        mensaje (string): recibe una cadena de texto para cifrar
        clave (int): clave de cifrado
    """
    texto_cifrado = ""

    for letra in mensaje.upper():
        if letra in ALFABETO:
            posicion = ALFABETO.index(letra)
            nueva_posicion = (posicion + clave) % len(ALFABETO)
            nueva_letra = ALFABETO[nueva_posicion]
            texto_cifrado += nueva_letra
        else:
            texto_cifrado += letra

    return texto_cifrado
