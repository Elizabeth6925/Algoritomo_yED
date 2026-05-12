#b. determinar los personajes que participaron en más de 5 películas de la saga,
#además indicar la cantidad de películas en la que aparece;

from pila_muc import apilar, desapilar, esta_vacia


def personajes_mas_de_5_peliculas(pila):

    pila2 = []

    personajes = []

    while not esta_vacia(pila):

        personaje = desapilar(pila)

        if personaje["peliculas"] > 5:
            personajes.append(
                (personaje["nombre"], personaje["peliculas"])
            )

        apilar(pila2, personaje)

    while not esta_vacia(pila2):
        apilar(pila, desapilar(pila2))

    return personajes
