#dada una pila de personajes de Marvel Cinematic Universe (MCU), de los cuales se dispone de
#su nombre y la cantidad de películas de la saga en la que participó, implementar las funciones
#necesarias para resolver las siguientes actividades:

def crear_pila():
    
    pila = []
    personajes = [
        {"nombre": "Thor",            "peliculas": 8},
        {"nombre": "Spider-Man",      "peliculas": 8},
        {"nombre": "Capitán América", "peliculas": 9},
        {"nombre": "black Widow",     "peliculas": 7},
        {"nombre": "black Panther",   "peliculas": 6},
        {"nombre": "Hulk",            "peliculas": 7},
        {"nombre": "Viuda Negra",     "peliculas": 7},
        {"nombre": "Doctor Strange",  "peliculas": 5},
        {"nombre": "Groot",           "peliculas": 5},
        {"nombre": "Clint Barton",    "peliculas": 6},
        {"nombre": "Rocket Raccoon",  "peliculas": 5},
        {"nombre": "Capitana Marvel", "peliculas": 4},
        {"nombre": "Scarlet Witch",   "peliculas": 6},
        {"nombre": "Gamora",          "peliculas": 4},
        {"nombre": "Drax",            "peliculas": 4},  
        {"nombre": "Deadpool",        "peliculas": 3},
        {"nombre": "Nebula",          "peliculas": 6},
        {"nombre": "Wanda Maximoff",  "peliculas": 6},
        {"nombre": "Iron Man",        "peliculas": 10},
        {"nombre": "nick Fury",       "peliculas": 7},
        {"nombre": "Captain America", "peliculas": 9},
        {"nombre": "Thanos",          "peliculas": 6},
        {"nombre": "Loki",            "peliculas": 7},
        {"nombre": "Dormammu",        "peliculas": 2},
        {"nombre": "Hela",            "peliculas": 1},
        {"nombre": "Ultron",          "peliculas": 2},
        {"nombre": "Cráneo Rojo",     "peliculas": 3},
        {"nombre": "Baron Zemo",       "peliculas": 3},
        {"nombre": "Mysterio",        "peliculas": 2},
        {"nombre": "Gorr",            "peliculas": 1},
    ]
    for p in personajes:
        pila.append(p) 
    return pila



def esta_vacia(pila):
    return len(pila) == 0

def cima(pila):
    if not esta_vacia(pila):
        return pila[-1]
    return None

def desapilar(pila):
    if not esta_vacia(pila):
        return pila.pop()
    return None

def apilar(pila, elemento):
    pila.append(elemento)


