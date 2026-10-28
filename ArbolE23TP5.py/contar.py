# d. determinar los 3 héroes o dioses que derrotaron mayor cantidad de criaturas;

def contar_derrotas(nodo, derrotas):
    if nodo is not None:
        contar_derrotas(nodo.izq, derrotas)

        if nodo.derrotado_por:
            derrotas[nodo.derrotado_por] = derrotas.get(nodo.derrotado_por, 0) + 1

        contar_derrotas(nodo.der, derrotas)
        