"""
Metodo principal para creacion de API
"""

# pylint: disable=E0611


from fastapi import FastAPI

from app.funciones.cifrado_cesar import cifrado_cesar

APP = FastAPI()


@APP.get("/")
def home():
    """_summary_

    Returns:
        _type_: _description_
    """
    return {"Hola": "Mundo 123"}


@APP.get("/cifrado-cesar")
def cifrado_cesar_api(texto, clave):
    """_summary_

    Args:
        texto (_type_): _description_
        clave (_type_): _description_
    """
    resultado = cifrado_cesar(mensaje=texto, clave=int(clave))

    return {"Resultado": resultado}
