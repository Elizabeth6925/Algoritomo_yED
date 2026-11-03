#Ejercicio 2: Dado un grafo no dirigido con personajes de la saga Star Wars: 

# archivo: grafoSW.py

import json
from graph import Graph

def crear_grafo_star_wars(ruta_archivo):
    """
    Lee el archivo JSON de Star Wars y devuelve un grafo no dirigido.
    """
    with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
        datos = json.load(archivo)

    # crea el grafo no dirigido
    star_wars = Graph(is_dir=False)

    # 1. Carga todos los personajes como vértices
    for p in datos['personajes']:
        star_wars.add_vertex(p['nombre'])

    # 2. Carga las aristas (relaciones)
  
    aristas_cargadas = set()

    for p in datos['personajes']:
        origen = p['nombre']
        for arista in p['aristas']:
            destino = arista['destino']
            peso = arista['episodios']
            
            # Normaliza la arista (ej: "Luke-Leia" es lo mismo que "Leia-Luke")

            conexion = tuple(sorted([origen, destino]))
            
            if conexion not in aristas_cargadas:
                star_wars.add_edge(peso, origen, destino)
                aristas_cargadas.add(conexion)

    return star_wars

