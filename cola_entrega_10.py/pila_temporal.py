# c. utilizar una pila para almacenar temporáneamente las notificaciones producidas entre las
# 11:43 y las 15:57, y determinar cuántas son.

from contar_notificacion import buscar_notificaciones

def pila_notificaciones(gestor, inicio="11:43", fin="15:57"):
    resultados, cantidad = buscar_notificaciones(gestor, hora_inicio=inicio, hora_fin=fin)

    pila = []  # pila LIFO
    for n in resultados:
        pila.append(n)

    return pila, cantidad
