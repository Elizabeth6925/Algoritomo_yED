# d. determinar cuántos superhéroes hay el árbol

def contar_heroes(root):
    if root is None:
        return 0
    
    # Verifica si el nodo actual es un héroe (is_villain == False)
    es_heroe = root.other_values and not root.other_values.get('is_villain')
    
    # Cuenta el nodo actual si es un héroe y suma los conteos de los subárboles izquierdo y derecho
    return (1 if es_heroe else 0) + contar_heroes(root.left) + contar_heroes(root.right)


# Conteo general: Cuenta todos los nodos de cualquier árbol
def contar_nodos(root):
    if root is None:
        return 0
    
    return 1 + contar_nodos(root.left) + contar_nodos(root.right)