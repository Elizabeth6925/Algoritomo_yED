# g. generar un bosque a partir de este árbol, un árbol debe contener a los superhéroes y otro a
# los villanos, luego resolver las siguiente tareas:
# I. determinar cuántos nodos tiene cada árbol;
# II. realizar un barrido ordenado alfabéticamente de cada árbol.

# bosque.py

def generar_bosque(root, arbol_heroes, arbol_villanos):
    if root is not None:
        generar_bosque(root.left, arbol_heroes, arbol_villanos)
        
        es_villano = root.other_values and root.other_values.get('is_villain') is True
        if es_villano:
            arbol_villanos.insert_node(root.value, root.other_values)
        else:
            arbol_heroes.insert_node(root.value, root.other_values)
            
        generar_bosque(root.right, arbol_heroes, arbol_villanos)

        