# a. escribir una función que elimine de la cola todas las notificaciones de Facebook;

from collections import deque

def eliminar_por_app(cola, app):
    cola_sin_notf = deque()
    eliminadas = 0

    while cola:
        hora, nombre_app, mensaje = cola.popleft()
        if nombre_app != app:
            cola_sin_notf.append((hora, nombre_app, mensaje))
        else:
            eliminadas += 1

    return eliminadas, cola_sin_notf
