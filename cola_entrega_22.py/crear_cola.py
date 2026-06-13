#22. Se tienen una cola con personajes de Marvel Cinematic Universe (MCU), 
# de los cuales se conoce el nombre del personaje, el nombre del superhéroe y su género (Masculino M y FemeninoF)
# –por ejemplo {Tony Stark, Iron Man, M}, {Steve Rogers, Capitán América, M}, {Natasha Ro-manoff, Black Widow, F},
#  etc., desarrollar un algoritmo que resuelva las siguientes actividades:

def crear_cola():
    return []

def esta_vacia(cola):
    return len(cola) == 0

def encolar(cola, elemento):
    cola.append(elemento)

def desencolar(cola):
    if not esta_vacia(cola):
        return cola.pop(0)
    return None

def frente(cola):
    if not esta_vacia(cola):
        return cola[0]
    return None


