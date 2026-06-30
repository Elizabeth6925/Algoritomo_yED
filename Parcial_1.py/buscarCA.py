#funcion recursiva  para buscar, determinar si Capitan America esta en la lista.

def buscar_capitan(lista, indice: int = 0) -> bool:

    if indice >= len(lista):

        return "no esta en la lista "
    
    if lista[indice].name == "Captain America":

        return "si esta en la lista"
    
    return buscar_capitan(lista, indice + 1)

