
# a. realizar un listado ordenado por canción, por banda o artista y por año de lanzamiento,
# utilizando el método que sea más optimo para cada tipo de dato;

def quicksort_por_campo(lista, campo):
    """  Item A: Ordena campos de texto ('cancion' o 'artista') """
    if len(lista) <= 1:
        return lista
    
    pivote = lista[0]
    menores = [x for x in lista[1:] if x[campo].lower() <= pivote[campo].lower()]
    mayores = [x for x in lista[1:] if x[campo].lower() > pivote[campo].lower()]
    
    return quicksort_por_campo(menores, campo) + [pivote] + quicksort_por_campo(mayores, campo)


def counting_sort_por_anio(lista):
    """ Item A: Ordena el campo entero 'anio' """
    if not lista:
        return lista
    
    min_anio = min(c["anio"] for c in lista)
    max_anio = max(c["anio"] for c in lista)
    rango = max_anio - min_anio + 1
    
    conteo = [0] * rango
    for c in lista:
        conteo[c["anio"] - min_anio] += 1
        
    resultado = []
    for i in range(rango):
        anio_actual = min_anio + i
        coincidencias = [c for c in lista if c["anio"] == anio_actual]
        resultado.extend(coincidencias)
        
    return resultado


def ordenar_por_criterio(lista, opcion_criterio):
    """ Selecciona y ejecuta el método de ordenamiento. """
    if opcion_criterio == "1":
        return quicksort_por_campo(lista, "cancion"), "Nombre de Canción)"
    elif opcion_criterio == "2":
        return quicksort_por_campo(lista, "artista"), "Banda o Artista )"
    elif opcion_criterio == "3":
        return counting_sort_por_anio(lista), "Año de Lanzamiento )"
    else:
        return None, None