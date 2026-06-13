# a. determinar el nombre del personaje de la superhéroe Capitana Marvel;

from crear_cola import desencolar, encolar, esta_vacia

def personaje_de_capitana_marvel(cola):
    resultado = None
    aux = []
    
    while not esta_vacia(cola):
        p = desencolar(cola)
        if p["nombre_heroe"].lower() == "capitana marvel":
            resultado = p["nombre_real"]
        aux.append(p)
    
    for p in aux:
        encolar(cola, p)
    
    return resultado

