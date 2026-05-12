
#a. determinar en qué posición se encuentran Rocket Raccoon y Groot, 
# tomando como posición uno la cima de la pila;


from pila_muc import apilar, desapilar, esta_vacia


def posiciones_rocket_groot(pila):

    pila2 = []

    posicion = 1

    pos_rocket = -1
    pos_groot = -1

    while not esta_vacia(pila):

        datos = desapilar(pila)

        nombre = datos["nombre"]

        if nombre == "Rocket Raccoon":
            pos_rocket = posicion

        if nombre == "Groot":
            pos_groot = posicion

        apilar(pila2, datos)

        posicion += 1

    while not esta_vacia(pila2):
        apilar(pila, desapilar(pila2))

    print("Rocket Raccoon está en la posición:", pos_rocket)
    print("Groot está en la posición:", pos_groot)