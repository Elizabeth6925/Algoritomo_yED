def busqueda_lineal(lista, valor):
    valor = valor.lower()
    for i, elemento in enumerate(lista):
        if elemento.lower() == valor:
            return i
    return -1
 