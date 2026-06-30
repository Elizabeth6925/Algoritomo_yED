#Determinar en que posicion esta The Thing y Rocket Raccoon.

def buscar_posicion(lista, nombre: str, indice: int = 0):
    if indice >= len(lista):
        return f"{nombre} no está en la lista"
    if lista[indice].name == nombre:
        return f"{nombre} está en la posición {indice}"
    return buscar_posicion(lista, nombre, indice + 1)

