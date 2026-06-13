# f. determinar si el personaje Carol Danvers se encuentra en la cola e indicar su nombrede de superhéroes.
from crear_cola import crear_cola, desencolar, encolar, esta_vacia

def encontrar_carol_danvers(cola):
    resultado = None
    aux = crear_cola()
    
    while not esta_vacia(cola):
        p = desencolar(cola)
        if p["nombre_real"].lower() == "carol danvers":
            resultado = p["nombre_heroe"]
        encolar(aux, p)
    
    while not esta_vacia(aux):
        encolar(cola, desencolar(aux))
    
    return resultado