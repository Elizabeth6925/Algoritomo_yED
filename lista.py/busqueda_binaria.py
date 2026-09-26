def busqueda_binaria(lista, valor):
    valor = valor.lower()
    inicio, fin = 0, len(lista) - 1
    while inicio <= fin:
        medio = (inicio + fin) // 2
        elemento = lista[medio].lower()
        if elemento == valor:
            return medio
        elif elemento < valor:
            inicio = medio + 1
        else:
            fin = medio - 1
    return -1
 