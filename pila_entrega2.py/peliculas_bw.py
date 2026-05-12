#c. determinar en cuantas películas participo la Viuda Negra (Black Widow);
from pila_muc import apilar, desapilar, esta_vacia


def peliculas_black_widow(pila):

    pila2 = []

    cantidad = "no encontrada"

    while not esta_vacia(pila):

        personaje = desapilar(pila)

        if personaje["nombre"].lower() == "viuda negra":
            cantidad = personaje["peliculas"]

        apilar(pila2, personaje)

    while not esta_vacia(pila2):
        apilar(pila, desapilar(pila2))

    return cantidad