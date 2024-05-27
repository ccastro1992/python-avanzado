"""
Pruebas para comprobar el funcionamiento de app hash
"""

import pytest

from app.funciones.hashing import text_hash


@pytest.mark.parametrize(
    "mensaje,hash_m",
    [
        ("hola", "b221d9dbb083a7f33428d7c2a3c3198ae925614d70210e28716ccaa7cd4ddb79"),
        # ("hi", "uewerwesdkdfsdf"),
        ("mundo", "cb9c245f6cf4910aca447a02e910139b5456d63d53be538e386ed48472eaca5f"),
    ],
)
def test_text_hash(mensaje, hash_m):
    """
    _summary_
    """
    esperado_sha256 = hash_m
    salida = text_hash(mensaje=mensaje)
    assert salida == esperado_sha256
