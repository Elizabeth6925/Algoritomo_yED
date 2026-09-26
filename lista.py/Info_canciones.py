# f. mostrar toda la información de las canciones “Fake tales of San Francisco” y “Black hole sun”.

def busqueda_binaria_cancion(lista_ordenada, cancion_buscada):
    
    inicio = 0
    fin = len(lista_ordenada) - 1
    buscado = cancion_buscada.lower()

    while inicio <= fin:
        medio = (inicio + fin) // 2
        actual = lista_ordenada[medio]["cancion"].lower()

        if actual == buscado:
            return lista_ordenada[medio]
        elif actual < buscado:
            inicio = medio + 1
        else:
            fin = medio - 1

    return None