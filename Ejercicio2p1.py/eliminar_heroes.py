#Eliminar a Electro y Baron Zemo de la lista y mostrar su información si estaba en la lista.

def eliminar_heroe(lista, nombre: str, indice: int = 0):
    if indice >= len(lista):
        return None
    if lista[indice].name == nombre:
        return lista.pop(indice)
    return eliminar_heroe(lista, nombre, indice + 1)