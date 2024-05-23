"""
Este es el archivo principal
"""

from funciones.cifrado_cesar import cifrado_cesar

MENSAJE = "Hola mundo"
CLAVE = 7

resultado = cifrado_cesar(MENSAJE, CLAVE)

print(resultado)
