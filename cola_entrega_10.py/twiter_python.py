# b. escribir una función que muestre todas las notificaciones de Twitter, cuyo mensaje incluya la palabra ‘Python’,
# si perder datos en la cola;

from collections import deque

def mostrar_twit_python(cola):

    aux = deque()
    encontradas = 0

    print("  Notificaciones de Twitter que mencionan 'Python'")

    while cola:
        hora, app, mensaje = cola.popleft()

        if app.lower() == "twitter" and "python" in mensaje.lower():
            print(f"  [{hora}]  {app:<12}  {mensaje}")
            encontradas += 1

        aux.append((hora, app, mensaje))   # siempre, no solo si cumple

    while aux:
        cola.append(aux.popleft())

    if encontradas == 0:
        
        print("  (ninguna notificacion encontrada)")

    print(f"  Total encontradas: {encontradas}")


    return encontradas