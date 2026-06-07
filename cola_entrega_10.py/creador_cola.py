#Dada una cola con las notificaciones de las aplicaciones de redes sociales de un Smartphone,
# de las cual se cuenta con la hora de la notificación, la aplicación que la emitió y el mensaje


from collections import deque


def crear_cola():
   
    cola_original = deque()

    cola_original.append(("09:12", "WhatsApp",  "Hola! Cómo estás?"))
    cola_original.append(("10:05", "Facebook",  "Juan te etiquetó en una foto"))
    cola_original.append(("11:43", "Twitter",   "Nuevo tweet sobre Python y sus librerías"))
    cola_original.append(("12:20", "Instagram", "María comenzó a seguirte"))
    cola_original.append(("12:55", "Facebook",  "Tienes 3 nuevas solicitudes de amistad"))
    cola_original.append(("13:30", "Twitter",   "Python 3.13 fue lanzado hoy"))
    cola_original.append(("14:10", "WhatsApp",  "Reunión en 20 minutos"))
    cola_original.append(("15:00", "Facebook",  "Le gustó tu publicación"))
    cola_original.append(("15:45", "Twitter",   "Tips de JavaScript para 2025"))
    cola_original.append(("15:57", "Instagram", "Tu historia venció"))
    cola_original.append(("16:30", "Twitter",   "Python es el lenguaje más popular"))
    cola_original.append(("17:02", "WhatsApp",  "Pedro: nos vemos mañana"))
    cola_original.append(("18:15", "Facebook",  "Recuerda tu evento de mañana"))

    return cola_original 


def mostrar_cola(cola_original, titulo="Cola"):


    print("\n{}".format("─" * 62))
    print("  {}  ({} notificaciones)".format(titulo, len(cola_original)))
    print("{}".format("─" * 62))

    for hora, app, mensaje in cola_original:
        print("  [{}]  {:<12} → {}".format(hora, app, mensaje))

    print("{}".format("─" * 62))