# b. listar los villanos ordenados alfabéticamente

def listar_villanos_alfabeticamente(root):
    if root is not None:
        listar_villanos_alfabeticamente(root.left)
        if root.other_values and root.other_values.get('is_villain') is True:
            print(f"- {root.value}")
        listar_villanos_alfabeticamente(root.right)


# c. mostrar todos los superhéroes que empiezan con C;

def listar_heroes_con_c(root):
    if root is not None:
        listar_heroes_con_c(root.left)
        # Verifica que sea héroe (is_villain == False) y empiece con 'C'
        es_heroe = root.other_values and not root.other_values.get('is_villain')
        empieza_con_c = root.value.startswith('C')
        
        if es_heroe and empieza_con_c:
            print(f"- {root.value}")
            
        listar_heroes_con_c(root.right)


# f. listar los superhéroes ordenados de manera descendente;

def listar_heroes_descendente(root):
    if root is not None:
        # 1. Recorre primero la derecha (los nombres alfabéticamente mayores)
        listar_heroes_descendente(root.right)
        
        # 2. Muestra solo si es héroe
        es_heroe = root.other_values and not root.other_values.get('is_villain')
        if es_heroe:
            print(f"- {root.value}")
            
        # 3. Recorre al final la izquierda (los nombres alfabéticamente menores)
        listar_heroes_descendente(root.left)

        