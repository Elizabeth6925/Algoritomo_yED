# Dada una cola con las notificaciones de las aplicaciones de redes sociales de un Smartphone,
# de las cual se cuenta con la hora de la notificación, la aplicación que la emitió y el mensaje,
# resolver las siguientes actividades:

# a. escribir una función que elimine de la cola todas las notificaciones de Facebook;
# b. escribir una función que muestre todas las notificaciones de Twitter, cuyo mensaje incluya la palabra ‘Python’,
# si perder datos en la cola;
# c. utilizar una pila para almacenar temporáneamente las notificaciones producidas entre las
# 11:43 y las 15:57, y determinar cuántas son.



from creador_cola import crear_cola , mostrar_cola

cola = crear_cola()

mostrar_cola(cola,"cola original ")

#a
from eliminar import eliminar_por_app

# Eliminar todas las notificaciones de Facebook
eliminadas, cola_sin_notf = eliminar_por_app(cola, "Facebook")

print(f"\nSe eliminaron {eliminadas} notificaciones de Facebook")

# Mostrar la cola auxiliar con el mismo formato
mostrar_cola(cola_sin_notf, "Cola sin notificaciones de Facebook")