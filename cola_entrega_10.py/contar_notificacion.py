# esta parte sirve para resolver twiter_python y pila_temporal puntos b y c respectivmente 

def buscar_notificaciones(gestor, app=None, palabra=None, hora_inicio=None, hora_fin=None):
    """
    Busca notificaciones según filtros opcionales:
    - app: nombre de la aplicación (ej. "Twitter")
    - palabra: palabra clave en el mensaje (ej. "Python")
    - hora_inicio, hora_fin: rango horario en formato "HH:MM"

    Devuelve la lista de notificaciones encontradas y la cantidad.
    """
    resultados = gestor.lista

    # Filtrar por aplicación
    if app:
        resultados = [n for n in resultados if n["app"].lower() == app.lower()]

    # Filtrar por palabra en mensaje
    if palabra:
        resultados = [n for n in resultados if palabra.lower() in n["mensaje"].lower()]

    # Filtrar por rango horario
    if hora_inicio and hora_fin:
        from datetime import datetime
        inicio = datetime.strptime(hora_inicio, "%H:%M")
        fin = datetime.strptime(hora_fin, "%H:%M")
        resultados = [
            n for n in resultados
            if inicio <= datetime.strptime(n["hora"], "%H:%M") <= fin
        ]

    return resultados, len(resultados)
