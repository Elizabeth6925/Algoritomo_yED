# e. Doctor Strange en realidad está mal cargado. Utilice una búsqueda por proximidad para encontrarlo en el árbol y modificar su nombre

def modificar_doctor_strange_proximidad(arbol, nuevo_nombre="Dr Strange"):
    nodo_encontrado = [None]

    # Recorrido para buscar por proximidad flexible
    def __buscar_proximidad(root):
        if root is not None and nodo_encontrado[0] is None:
            __buscar_proximidad(root.left)
            
            val_lower = root.value.lower()
            # Si empieza con 'dr' o contiene 'stra' (cubre 'Strannnnnge')
            if val_lower.startswith("dr") or "stra" in val_lower:
                nodo_encontrado[0] = root
                return
                
            __buscar_proximidad(root.right)

    __buscar_proximidad(arbol.root)

    # Si lo encuentra, elimina e reinserta con el nombre correcto
    if nodo_encontrado[0] is not None:
        nombre_viejo = nodo_encontrado[0].value
        datos = nodo_encontrado[0].other_values
        
        if isinstance(datos, dict):
            datos['name'] = nuevo_nombre

        arbol.delete_node(nombre_viejo)
        arbol.insert_node(nuevo_nombre, other_value=datos)
        print(f"¡Se encontró '{nombre_viejo}' por proximidad y se actualizó a '{nuevo_nombre}'!")
        return True
    else:
        print("No se encontró ningún personaje que coincida.")
        return False