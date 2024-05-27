"""
Modulo para obtener el hash de un string
"""

import hashlib


def text_hash(mensaje):
    """
    _summary_
    Returns:
        _type_: _description_
    """
    entorno_hash = hashlib.sha256()
    entorno_hash.update(mensaje.encode("UTF-8"))
    salida = entorno_hash.hexdigest()
    return salida
