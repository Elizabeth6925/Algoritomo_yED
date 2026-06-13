
from crear_cola import crear_cola, encolar, esta_vacia

def carga_cola():
    cola = crear_cola()
    personajes = [
        {"nombre_real": "Thor Odinson",          "nombre_heroe": "Thor",            "genero": "M"},
        {"nombre_real": "Peter Parker",          "nombre_heroe": "Spider-Man",      "genero": "M"},
        {"nombre_real": "Steve Rogers",          "nombre_heroe": "Capitán América", "genero": "M"},
        {"nombre_real": "Natasha Romanoff",      "nombre_heroe": "Black Widow",     "genero": "F"},
        {"nombre_real": "T'Challa",              "nombre_heroe": "Black Panther",   "genero": "M"},
        {"nombre_real": "Bruce Banner",          "nombre_heroe": "Hulk",            "genero": "M"},
        {"nombre_real": "Stephen Strange",       "nombre_heroe": "Doctor Strange",  "genero": "M"},
        {"nombre_real": "Groot",                 "nombre_heroe": "Groot",           "genero": "M"},
        {"nombre_real": "Clint Barton",          "nombre_heroe": "Ojo de Halcón",   "genero": "M"},
        {"nombre_real": "Rocket Raccoon",        "nombre_heroe": "Rocket Raccoon",  "genero": "M"},
        {"nombre_real": "Carol Danvers",         "nombre_heroe": "Capitana Marvel", "genero": "F"},
        {"nombre_real": "Wanda Maximoff",        "nombre_heroe": "Scarlet Witch",   "genero": "F"},
        {"nombre_real": "Gamora",                "nombre_heroe": "Gamora",          "genero": "F"},
        {"nombre_real": "Drax el Destructor",    "nombre_heroe": "Drax",            "genero": "M"},
        {"nombre_real": "Wade Wilson",           "nombre_heroe": "Deadpool",        "genero": "M"},
        {"nombre_real": "Nebula",                "nombre_heroe": "Nebula",          "genero": "F"},
        {"nombre_real": "Tony Stark",            "nombre_heroe": "Iron Man",        "genero": "M"},
        {"nombre_real": "Nick Fury",             "nombre_heroe": "Nick Fury",       "genero": "M"},
        {"nombre_real": "Thanos",                "nombre_heroe": "Thanos",          "genero": "M"},
        {"nombre_real": "Loki Laufeyson",        "nombre_heroe": "Loki",            "genero": "M"},
        {"nombre_real": "Dormammu",              "nombre_heroe": "Dormammu",        "genero": "M"},
        {"nombre_real": "Hela Odinsdottir",      "nombre_heroe": "Hela",            "genero": "F"},
        {"nombre_real": "Ultron",                "nombre_heroe": "Ultron",          "genero": "M"},
        {"nombre_real": "Johann Schmidt",        "nombre_heroe": "Cráneo Rojo",     "genero": "M"},
        {"nombre_real": "Helmut Zemo",           "nombre_heroe": "Baron Zemo",      "genero": "M"},
        {"nombre_real": "Quentin Beck",          "nombre_heroe": "Mysterio",        "genero": "M"},
        {"nombre_real": "Gorr",                  "nombre_heroe": "Gorr",            "genero": "M"},
    ]
    for p in personajes:
        encolar(cola, p)
    return cola


def mostrar_cola(cola):
    if esta_vacia(cola):
        print("La cola está vacía.")
        return
    print(f"{'Nombre Real':<25} {'Héroe':<20} {'Género'}")
    print("-" * 55)
    for p in cola:
        print(f"{p['nombre_real']:<25} {p['nombre_heroe']:<20} {p['genero']}")


