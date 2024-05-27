"""
Testing API
"""

# pylint: disable=E0611

from fastapi.testclient import TestClient

from ..main import app

CLIENT = TestClient(app)


def test_url_cifrado_cesar():
    """
    _summary_
    """
    respuesta = CLIENT.get("/cifrado-cesar?texto=mama&clave=1")
    assert respuesta.status_code == 200
    assert respuesta.json() == {"Resultado": "NBNB"}
