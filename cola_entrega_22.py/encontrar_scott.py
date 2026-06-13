# d. determinar el nombre del superhéroe del personaje Scott Lang;

from crear_cola import desencolar, encolar, esta_vacia, crear_cola

def heroe_de_scott_lang(cola):
    resultado = None
    aux = crear_cola()
    
    while not esta_vacia(cola):
        p = desencolar(cola)
        if p["nombre_real"].lower() == "scott lang":
            resultado = p["nombre_heroe"]
        encolar(aux, p)

    
    while not esta_vacia(aux):

        encolar(cola, desencolar(aux))
    
    return resultado

