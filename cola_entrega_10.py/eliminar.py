# a. escribir una función que elimine de la cola todas las notificaciones de Facebook;

from collections import deque


def eliminar_por_app(cola_original, app_objetivo):
  
    cola_resultado = deque()
    eliminadas = 0

    while cola_original:
        hora, app, mensaje = cola_original.popleft()

        if app.lower() == app_objetivo.lower():
            eliminadas += 1          
            
        else:
            cola_resultado.append((hora, app, mensaje))   

    return eliminadas, cola_resultado