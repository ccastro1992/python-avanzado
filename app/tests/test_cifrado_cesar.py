"""
Pruebas unitarias
"""

import pytest

from app.funciones.cifrado_cesar import cifrado_cesar


@pytest.mark.parametrize(
    "entrada, clave, salida_esperada",
    [("mama", 1, "NBNB"), ("papa", 1, "QBQB"), ("a", 2, "C"), ("a", 1, "B")],
)
def test_cifrado_cesar(entrada, clave, salida_esperada):
    """Test para cifrado cesar"""
    texto_cifrado = cifrado_cesar(mensaje=entrada, clave=clave)
    assert texto_cifrado == salida_esperada
