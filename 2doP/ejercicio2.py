# Ejercicio 2: Dado un grafo no dirigido con personajes de la saga Star Wars, implementar los algoritmos necesarios para resolver las siguientes tareas:
# A _cada vértice debe almacenar el nombre de un personaje, las aristas representan la cantidad de episodios en los que aparecieron juntos ambos personajes que se relacionan;
# B _hallar el árbol de expansión mínimo desde el vértice que contiene a: C-3PO, Yoda y Leia;
# C_ determinar cuál es el número máximo de episodio que comparten dos personajes, e indicar todos los pares de personajes que coinciden con dicho número;
# D_cargue al menos los siguientes personajes: Luke Skywalker, Darth Vader, Yoda, Boba Fett, C-3PO, Leia, Rey, Kylo Ren, Chewbacca, Han Solo, R2-D2, BB-8;
# E_calcule el camino mas ccorto desde: C-3PO a R2-D2 y desde Yoda a Darth Vader;
# F_indicar qué personajes aparecieron en los nueve episodios de la saga.



from graph import Graph
import heapq


# función auxiliar para reemplazar el dijkstra de graph.py

def dijkstra_corregido(grafo, origen, destino):
    if grafo.search(origen, 'value') is None or grafo.search(destino, 'value') is None:
        print(f"Error: Origen '{origen}' o destino '{destino}' no existen en el grafo.")
        return [], float('inf')
    
    distancias = {v.value: float('inf') for v in grafo}
    distancias[origen] = 0
    previos = {v.value: None for v in grafo}
    
    cola = [(0, origen)]
    
    while cola:
        dist_actual, nodo_actual = heapq.heappop(cola)
        
        if dist_actual > distancias[nodo_actual]:
            continue
            
        if nodo_actual == destino:
            break
            
        pos = grafo.search(nodo_actual, 'value')
        if pos is None: continue
        vertice = grafo[pos]
        
        for arista in vertice.edges:
            vecino = arista.destination
            peso = arista.weight
            nueva_dist = dist_actual + peso
            
            if nueva_dist < distancias[vecino]:
                distancias[vecino] = nueva_dist
                previos[vecino] = nodo_actual
                heapq.heappush(cola, (nueva_dist, vecino))
                
    camino = []
    actual = destino
    while actual is not None:
        camino.insert(0, actual)
        actual = previos[actual]
        
    if distancias[destino] == float('inf'):
        return [], float('inf')
        
    return camino, distancias[destino]


# PUNTO A y D: Carga del grafo (Vértices y Aristas)

print("\n. Cargando el grafo de Star Wars ")
star_wars = Graph(is_dir=False)

# Carga los personajes (vértices)
personajes = [
    "Luke Skywalker", "Darth Vader", "Yoda", "Boba Fett", "C-3PO", "Leia",
    "Rey", "Kylo Ren", "Chewbacca", "Han Solo", "R2-D2", "BB-8"
]
for p in personajes:
    star_wars.add_vertex(p)

# Carga las relaciones (aristas) con sus pesos (episodios)
# Usa un set para evitar duplicar las aristas (ida y vuelta)

relaciones = [
    (3, "Luke Skywalker", "Darth Vader"), (6, "Luke Skywalker", "Leia"),
    (5, "Luke Skywalker", "Han Solo"), (5, "Luke Skywalker", "Chewbacca"),
    (5, "Luke Skywalker", "C-3PO"), (5, "Luke Skywalker", "R2-D2"),
    (3, "Luke Skywalker", "Yoda"),
    (3, "Darth Vader", "Leia"), (3, "Darth Vader", "C-3PO"),
    (3, "Darth Vader", "R2-D2"), (2, "Darth Vader", "Yoda"),
    (2, "Darth Vader", "Boba Fett"),
    (3, "Yoda", "C-3PO"), (4, "Yoda", "R2-D2"), (1, "Yoda", "Chewbacca"),
    (2, "Boba Fett", "Han Solo"), (2, "Boba Fett", "Chewbacca"),
    (2, "Boba Fett", "C-3PO"), (2, "Boba Fett", "R2-D2"),
    (9, "C-3PO", "Leia"), (9, "C-3PO", "R2-D2"),
    (5, "C-3PO", "Han Solo"), (6, "C-3PO", "Chewbacca"),
    (8, "Leia", "R2-D2"), (5, "Leia", "Han Solo"), (5, "Leia", "Chewbacca"),
    (3, "Rey", "Kylo Ren"), (3, "Rey", "Chewbacca"),
    (2, "Rey", "R2-D2"), (3, "Rey", "C-3PO"), (3, "Rey", "BB-8"),
    (3, "Kylo Ren", "Chewbacca"), (3, "Kylo Ren", "BB-8"),
    (5, "Chewbacca", "Han Solo"), (6, "Chewbacca", "R2-D2"),
    (2, "R2-D2", "BB-8"), (2, "BB-8", "C-3PO")
]

aristas_cargadas = set()
for peso, u, v in relaciones:
    arista = tuple(sorted((u, v)))
    if arista not in aristas_cargadas:
        star_wars.add_edge(peso, u, v)
        aristas_cargadas.add(arista)

print("¡Grafo creado con éxito! (12 personajes cargados)")


# PUNTO B: Árbol de Expansión Mínimo (MST)

print("\nÁrbol de Expansión Mínimo (MST) ")
# El profe pide desde C-3PO, Yoda y Leia. 
# Como el método kruskal de tu grafo toma un origen, mostramos los 3.
for origen in ["C-3PO", "Yoda", "Leia"]:
    print(f"\nMST desde el vértice '{origen}':")
    mst_str = star_wars.kruskal(origen) 
    
    peso_total_mst = 0
    if mst_str:
        for edge in mst_str.split(';'):
            try:
                origin, destination, weight = edge.split('-')
                print(f"  {origin} -- {destination} (episodios: {weight})")
                peso_total_mst += int(weight)
            except ValueError:
                pass
    print(f"  Peso total del MST: {peso_total_mst}")


# PUNTO C: Máximo número de episodios compartidos

print("\n Máximo número de episodios compartidos")
max_episodios = 0
pares_max = []

# Recorre todas las aristas del grafo
aristas_revisadas = set()
for vertice in star_wars:
    for arista in vertice.edges:
        # Normalizamos para no revisar la misma arista dos veces (ida y vuelta)
        par = tuple(sorted([vertice.value, arista.destination]))
        if par not in aristas_revisadas:
            aristas_revisadas.add(par)
            
            if arista.weight > max_episodios:
                max_episodios = arista.weight
                pares_max = [par]
            elif arista.weight == max_episodios:
                pares_max.append(par)

print(f"El número máximo de episodios compartidos es: {max_episodios}")
print("Los pares de personajes que coinciden con ese número son:")
for p1, p2 in pares_max:
    print(f"  - {p1} y {p2}")


# PUNTO E: Caminos más cortos (Dijkstra)

print("\n Caminos más cortos ")

# A) De C-3PO a R2-D2
camino, distancia = dijkstra_corregido(star_wars, "C-3PO", "R2-D2")
print(f"De C-3PO a R2-D2:")
print(f"  Camino: {' -> '.join(camino)}")
print(f"  Total de episodios compartidos en el camino: {distancia}")

# B) De Yoda a Darth Vader
camino, distancia = dijkstra_corregido(star_wars, "Yoda", "Darth Vader")
print(f"De Yoda a Darth Vader:")
print(f"  Camino: {' -> '.join(camino)}")
print(f"  Total de episodios compartidos en el camino: {distancia}")


# PUNTO F: Personajes que aparecieron en los 9 episodios

print("\nPersonajes que aparecieron en los 9 episodios")
# Si un personaje tiene una arista con peso 9, significa que compartió pantalla
# con otro personaje en 9 episodios (o que apareció en los 9).
personajes_9_episodios = set()

for vertice in star_wars:
    for arista in vertice.edges:
        if arista.weight == 9:
            personajes_9_episodios.add(vertice.value)
            personajes_9_episodios.add(arista.destination)

if personajes_9_episodios:
    for p in personajes_9_episodios:
        print(f"  - {p}")
else:
    print("  No se encontraron personajes con aristas de peso 9.")