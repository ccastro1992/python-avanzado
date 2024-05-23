"""
Prueba de encriptado simetrico
"""

import pytest
from cryptography.fernet import Fernet

from app.funciones.encriptado import desencriptando_texto, encriptando_texto


@pytest.mark.parametrize(
    "mensaje, llave",
    [
        (b"mama", b"ICN-bIsF9-imvWjKwHANyCD2IsN7ZFP6ee9clruwevw="),
        (b"papa", b"ICN-bIsF9-imvWjKwHANyCD2IsN7ZFP6ee9clruwevw="),
    ],
)
def test_encriptando_texto(mensaje, llave):
    """Test para cifrado cesar"""
    salida = encriptando_texto(mensaje, llave)
    mensaje_desencriptado = desencriptando_texto(salida, llave)

    assert mensaje == mensaje_desencriptado
