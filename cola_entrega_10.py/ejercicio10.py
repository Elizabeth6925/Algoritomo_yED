# Dada una cola con las notificaciones de las aplicaciones de redes sociales de un Smartphone,
# de las cual se cuenta con la hora de la notificación, la aplicación que la emitió y el mensaje,
# resolver las siguientes actividades:

# a. escribir una función que elimine de la cola todas las notificaciones de Facebook;
# b. escribir una función que muestre todas las notificaciones de Twitter, cuyo mensaje incluya la palabra ‘Python’,
# si perder datos en la cola;
# c. utilizar una pila para almacenar temporáneamente las notificaciones producidas entre las
# 11:43 y las 15:57, y determinar cuántas son   

from creador_cola import crear_cola , mostrar_cola
from eliminar import eliminar_por_app
from twiter_python import mostrar_twit_python
from pila_temporal import notific_hora , mostrar_pila
# ── Creacion de la cola original ──

cola = crear_cola()
mostrar_cola(cola, "Cola original")
 
 
# ── Inciso a: eliminar notificaciones de Facebook ──

print("\n\n>>> INCISO A: Eliminar notificaciones de Facebook")
 
eliminadas, cola_sin_fb = eliminar_por_app(cola, "Facebook")
 
print(f"\n  Se eliminaron {eliminadas} notificaciones de Facebook.")
mostrar_cola(cola_sin_fb, "Cola sin notificaciones de Facebook")
 
 
# ── Inciso b: mostrar tweets con 'Python' sin perder datos ───

print("\n\n>>> INCISO B: Notificaciones de Twitter con la palabra 'Python'")
 
# Se trabaja sobre la cola resultante del inciso a
encontradas = mostrar_twit_python(cola_sin_fb)
 

mostrar_cola(cola_sin_fb, "Cola tras inciso b (debe conservar todos sus datos)")
 
 
# ── Inciso c: pila con notificaciones entre 11:43 y 15:57 ───

print("\n\n>>> INCISO C: Notificaciones entre las 11:43 y las 15:57")
 
pila, cantidad = notific_hora(cola_sin_fb, "11:43", "15:57")
 
mostrar_pila(pila, "Pila de notificaciones 11:43 - 15:57")

print(f"\n  Total de notificaciones en el rango: {cantidad}")
 