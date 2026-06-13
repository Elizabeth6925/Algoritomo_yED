# e. mostrar todos datos de los superhéroes o personaje cuyos nombres comienzancon la letra S;

from crear_cola import crear_cola, desencolar, encolar, esta_vacia

def nombres_con_s(cola):
    por_nombre_real = crear_cola()
    por_nombre_heroe = crear_cola()
    aux = crear_cola()
    
    while not esta_vacia(cola):
        p = desencolar(cola)
        if p["nombre_real"].startswith("S"):
            encolar(por_nombre_real, p)
        if p["nombre_heroe"].startswith("S"):
            encolar(por_nombre_heroe, p)
        encolar(aux, p)
    
    while not esta_vacia(aux):
        encolar(cola, desencolar(aux))
    
    return por_nombre_real, por_nombre_heroe
