"""
Encriptacion Simetrica
"""

from cryptography.fernet import Fernet


def encriptando_texto(mensaje, llave):
    """_summary_

    Args:
        mensaje (str): _description_
        llave (str): _description_

    Returns:
        str: _description_
    """

    # llave = Fernet.generate_key()
    entorno_cifrado = Fernet(llave)

    mensaje_encriptado = entorno_cifrado.encrypt(mensaje)

    return mensaje_encriptado


def desencriptando_texto(mensaje, llave):
    """_summary_

    Args:
        mensaje (str): _description_
        llave (str): _description_

    Returns:
        str: _description_
    """

    entorno_cifrado = Fernet(llave)

    mensaje_desencriptado = entorno_cifrado.decrypt(mensaje)

    return mensaje_desencriptado
