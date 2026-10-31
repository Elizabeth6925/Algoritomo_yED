# 5. Cargar el esquema de red de la siguiente figura en un grafo e implementar los algoritmos necesarios para resolver las tareas, listadas a continuación:
# a. cada nodo además del nombre del equipo deberá almacenar su tipo: pc, notebook, servidor, router, switch, impresora;
# b. realizar un barrido en profundidad y amplitud partiendo desde la tres notebook:
# Red Hat, Debian, Arch;
# c. encontrar el camino más corto para enviar a imprimir un documento desde la pc: Manjaro,
# Red Hat, Fedora hasta la impresora;
# d. encontrar el árbol de expansión mínima;
# e. determinar desde que pc (no notebook) es el camino más corto hasta el servidor “Guaraní”;
# f. indicar desde que computadora del switch 01 es el camino más corto
# al servidor “MongoDB”;
# g. cambiar la conexión de la impresora al router 02 y vuelva a resolver el punto b;
# h. debe utilizar un grafo no dirigido


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
    # punto a. Crear el grafo y cargar los nodos con sus tipos 
    
    red = Graph(is_dir=False) #punto h. grafo no dirigido 
    
    nodos = [
        ("Red Hat", "notebook"), ("Debian", "notebook"), ("Arch", "notebook"),
        ("Manjaro", "pc"), ("Ubuntu", "pc"), ("Mint", "pc"), ("Fedora", "pc"), ("Parrot", "pc"),
        ("Guaraní", "servidor"), ("MongoDB", "servidor"),
        ("Router 1", "router"), ("Router 2", "router"), ("Router 3", "router"),
        ("Switch 1", "switch"), ("Switch 2", "switch"),
        ("Impresora", "impresora")
    ]
    
    for nombre, tipo in nodos:
        red.add_vertex(nombre, other_values={'tipo': tipo})
        
    conexiones = [
        (50, "Router 2", "Router 3"), (37, "Router 2", "Router 1"), (43, "Router 1", "Router 3"),
        (25, "Router 2", "Red Hat"), (9, "Router 2", "Guaraní"),
        (29, "Router 1", "Switch 1"), (80, "Router 1", "Mint"),
        (40, "Router 3", "Manjaro"), (61, "Router 3", "Switch 2"),
        (17, "Switch 1", "Debian"), (18, "Switch 1", "Ubuntu"), (22, "Switch 1", "Impresora"),
        (12, "Switch 2", "Parrot"), (3, "Switch 2", "Fedora"), (56, "Switch 2", "Arch"), (5, "Switch 2", "MongoDB")
    ]
    
    for peso, origen, destino in conexiones:
        red.add_edge(peso, origen, destino)

    # print("--- a. Grafo de Red Creado (Topología Real) ---")
    # red.show()

    print("--- a. Nodos cargados con sus tipos ---")

    for vertice in red:
        print(f"Equipo: {vertice.value:<15} | Tipo: {vertice.other_values['tipo']}")
    print()

    # punto b. Barrido en profundidad y amplitud desde las notebooks 
    print("\n--- b. Barridos desde las notebooks (Red Hat, Debian, Arch) ---")
    notebooks = ["Red Hat", "Debian", "Arch"]
    for nb in notebooks:
        print(f"\nBarrido en PROFUNDIDAD desde '{nb}':")
        red.deep_show(nb)
        print(f"\nBarrido en AMPLITUD desde '{nb}':")
        red.amplitude_show(nb)
        print()

    # punto c. Camino más corto a la impresora 
    print("\n--- c. Camino más corto a la Impresora ---")
    pcs = ["Manjaro", "Red Hat", "Fedora"]
    
    for pc in pcs:
        # Usamos la función corregida en lugar del método del grafo
        camino, peso_total = dijkstra_corregido(red, pc, "Impresora")
        if camino:
            print(f"Desde '{pc}' a 'Impresora': Camino={' -> '.join(camino)}, Distancia={peso_total}")
        else:
            print(f"No se encontró camino desde '{pc}' a 'Impresora'.")

    # punto d. Árbol de expansión mínimo (MST) 

    print("\n--- d. Árbol de Expansión Mínimo (MST) ---")
    # Usamos tu método original de kruskal, ese funciona perfecto
    mst_str = red.kruskal("Router 1")
    
    print("Aristas del MST:")
    peso_total_mst = 0
    if mst_str:
        for edge in mst_str.split(';'):
            try:
                origin, destination, weight = edge.split('-')
                print(f"  {origin} -- {destination} (peso: {weight})")
                peso_total_mst += int(weight)
            except ValueError:
                print(f"  (Formato inesperado: {edge})")
                
    print(f"Peso total del MST: {peso_total_mst}")

    # punto e. Camino más corto desde PCs al servidor "Guaraní" 
    
    print("\n--- e. Camino más corto desde PCs a 'Servidor Guaraní' ---")
    todas_las_pcs = ["Manjaro", "Ubuntu", "Mint", "Fedora", "Parrot"]
    
    mejor_pc = None
    mejor_distancia = float('inf')
    mejor_camino = []

    for pc in todas_las_pcs:
        camino, peso_total = dijkstra_corregido(red, pc, "Guaraní")
        
        if camino:
            print(f"  Desde '{pc}' a 'Guaraní': Camino={' -> '.join(camino)}, Distancia={peso_total}")
            if peso_total < mejor_distancia:
                mejor_distancia = peso_total
                mejor_pc = pc
                mejor_camino = camino
        else:
            print(f"  No se encontró camino desde '{pc}' a 'Guaraní'")
                
    if mejor_pc:
        print(f"\n=> La PC con el camino más corto a Guaraní es '{mejor_pc}' con una distancia de {mejor_distancia}.")
        print(f"   El camino es: {' -> '.join(mejor_camino)}")
    else:
        print("\n=> No se encontró ningún camino a Guaraní desde las PCs.")

    # punto f. Camino más corto desde computadora del Switch 01 a MongoDB 

    print("\n--- f. Camino más corto desde PCs del Switch 1 a 'Servidor MongoDB' ---")
    computadoras_switch1 = ["Debian", "Ubuntu"] 
    
    for comp in computadoras_switch1:
        camino, peso_total = dijkstra_corregido(red, comp, "MongoDB")
        if camino:
            print(f"Desde '{comp}' a 'MongoDB': Camino={' -> '.join(camino)}, Distancia={peso_total}")

    # punto g. Cambiar conexión de la impresora al Router 2 y repetir barrido 
    
    print("\n--- g. Conexión de Impresora cambiada a Router 2 y nuevos barridos ---")
    
    # Eliminamos la arista antigua y agregamos la nueva

    red.delete_edge("Switch 1", "Impresora")
    red.add_edge(15, "Router 2", "Impresora") # Peso estimado 15
    
    print("Grafo modificado (Impresora conectada a Router 2).")
    
    print("\nNuevos barridos desde las notebooks:")
    for nb in notebooks:
        print(f"\nBarrido en PROFUNDIDAD desde '{nb}':")
        red.deep_show(nb)
        print(f"\nBarrido en AMPLITUD desde '{nb}':")
        red.amplitude_show(nb)
        print()

if __name__ == "__main__":
    main()