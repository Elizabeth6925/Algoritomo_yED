# d. agregar una nueva canción a la lista, y volver a realizar un listado ordenado por nombre de canción;

# se agrega una cancion de forma aleatoria y automatica y luego se reordena la lista por nombre de cancion
# from ordenar import quicksort_por_campo

# def agregar_y_reordenar(lista, cancion, artista, anio):

#     nueva_cancion = {
#         "cancion": cancion,
#         "artista": artista,
#         "anio": int(anio)
#     }
#     lista.append(nueva_cancion)
    
#     # Re-ordena la lista con el nuevo elemento usando Quicksort
#     lista_ordenada = quicksort_por_campo(lista, "cancion")
#     return lista, lista_ordenada

# permite al usuario agregar la cancion y reordena la lista por nombre de cancion

from ordenar import quicksort_por_campo

def agregar_y_reordenar(lista, cancion, artista, anio):

    nueva_cancion = {
        "cancion": cancion,
        "artista": artista,
        "anio": int(anio)
    }
    lista.append(nueva_cancion)
    
    # Re-ordena la lista con el nuevo elemento usando Quicksort
    lista_ordenada = quicksort_por_campo(lista, "cancion")
    return lista, lista_ordenada