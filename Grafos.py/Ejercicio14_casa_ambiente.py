# 14. Implementar sobre un grafo no dirigido los algoritmos necesario para dar solución a las siguientes tareas:

# a. cada vértice representar un ambiente de una casa: cocina, comedor, cochera, quincho,
# baño 1, baño 2, habitación 1, habitación 2, sala de estar, terraza, patio;

# b. cargar al menos tres aristas a cada vértice, y a dos de estas cárguele cinco,
# el peso de la arista es la distancia entre los ambientes, se debe cargar en metros;
# c. obtener el árbol de expansión mínima y 
# determine cuantos metros de cables se necesitan para conectar todos los ambientes;
# d. determinar cuál es el camino más corto desde la habitación 1 hasta la sala de estar para
# determinar cuántos metros de cable de red se necesitan para conectar el router con el Smart Tv.


from graph import Graph
import heapq


# FUNCIÓN AUXILIAR PARA REEMPLAZAR EL DIJKSTRA DE GRAPH.PY
# (Debido a un bug en la actualización de prioridades en el original)

def dijkstra_corregido(grafo, origen, destino):

    # Verificar si el origen y destino existen en el grafo
    if grafo.search(origen, 'value') is None or grafo.search(destino, 'value') is None:
        print(f"Error: Origen '{origen}' o destino '{destino}' no existen en el grafo.")
        return [], float('inf')
    
    # Crear un diccionario de distancias

    distancias = {v.value: float('inf') for v in grafo}
    distancias[origen] = 0
    previos = {v.value: None for v in grafo}
    
    # Cola de prioridad
    cola = [(0, origen)]
    
    while cola:
        dist_actual, nodo_actual = heapq.heappop(cola)
        
        if dist_actual > distancias[nodo_actual]:
            continue
            
        if nodo_actual == destino:
            break
            
        # Buscar el vértice en el grafo para obtener sus aristas
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
                
    # Reconstruir camino
    camino = []
    actual = destino
    while actual is not None:
        camino.insert(0, actual)
        actual = previos[actual]
        
    if distancias[destino] == float('inf'):
        return [], float('inf')
        
    return camino, distancias[destino]

# 

def main():
    # punto a. Crear el grafo y cargar los ambientes 
    casa = Graph(is_dir=False)
    
    ambientes = [
        "cocina", "comedor", "cochera", "quincho", "baño 1", "baño 2",
        "habitación 1", "habitación 2", "sala de estar", "terraza", "patio"
    ]
    
    for ambiente in ambientes:
        casa.add_vertex(ambiente)
    
    print("--- a. Grafo de la casa creado (Ambientes cargados) ---")
    for vertice in casa:
        print(f"- {vertice.value}")
    print()

    # punto b. Cargar las aristas (distancias en metros) 
    # Se asegura que cada nodo tenga al menos 3 aristas y se incluyen aristas con peso 5.
    conexiones = [
        # Cocina (3 aristas)
        (5, "cocina", "comedor"), (5, "cocina", "patio"), (8, "cocina", "baño 1"),
        # Comedor (3 aristas nuevas)
        (5, "comedor", "sala de estar"), (6, "comedor", "habitación 1"), 
        # Cochera (3 aristas)
        (12, "cochera", "patio"), (10, "cochera", "terraza"), (15, "cochera", "quincho"),
        # Quincho (2 aristas nuevas)
        (5, "quincho", "terraza"), (9, "quincho", "patio"), 
        # Baño 1 (2 aristas nuevas)
        (3, "baño 1", "habitación 1"), (6, "baño 1", "habitación 2"), 
        # Baño 2 (3 aristas)
        (2, "baño 2", "habitación 2"), (5, "baño 2", "sala de estar"), (8, "baño 2", "comedor"),
        # Habitación 1 (2 aristas nuevas)
        (4, "habitación 1", "habitación 2"), (10, "habitación 1", "sala de estar"), 
        # Habitación 2 (1 arista nueva)
        (7, "habitación 2", "sala de estar"),
        # Sala de estar (1 arista nueva)
        (7, "sala de estar", "terraza"), 
        # Terraza (1 arista nueva)
        (4, "terraza", "patio"), 
    ]

    # Usamos un set para evitar agregar aristas duplicadas (ida y vuelta)
    aristas_cargadas = set()
    for peso, u, v in conexiones:
        arista = tuple(sorted((u, v)))
        if arista not in aristas_cargadas:
            casa.add_edge(peso, u, v)
            aristas_cargadas.add(arista)

    print("--- b. Aristas cargadas (Distancias en metros) ---")
    casa.show()
    print()

    # punto c. Obtener el MST y calcular el total de metros de cable 
    print("--- c. Árbol de Expansión Mínimo (MST) para el cableado ---")
    mst_str = casa.kruskal("cocina") 
    
    print("Aristas del MST:")
    peso_total_mst = 0
    if mst_str:
        for edge in mst_str.split(';'):
            try:
                origin, destination, weight = edge.split('-')
                print(f"  {origin} -- {destination} (distancia: {weight} m)")
                peso_total_mst += int(weight)
            except ValueError:
                print(f"  (Formato inesperado: {edge})")
                
    print(f"\n=> Total de metros de cable necesarios para conectar todos los ambientes: {peso_total_mst} metros.")

    # punto d. Camino más corto de habitación 1 a sala de estar 
    print("\n--- d. Camino más corto para el cable de red ---")
    camino, peso_total = dijkstra_corregido(casa, "habitación 1", "sala de estar")
    
    if camino:
        print(f"El camino más corto desde 'habitación 1' hasta 'sala de estar' es:")
        print(f"  Camino: {' -> '.join(camino)}")
        print(f"  Distancia total: {peso_total} metros.")
        print(f"\n=> Se necesitan {peso_total} metros de cable de red para conectar el router con el Smart TV.")
    else:
        print("No se encontró un camino entre los ambientes.")

if __name__ == "__main__":
    main()