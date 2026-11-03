# Ejercicio 1: Se tiene los datos de Pokémons de las 9 generaciones cargados de manera aleatoria (1025 en total) de los cuales se conoce su nombre,
#  número, tipo/tipos, debilidad frente a tipo/tipos, si tiene mega evolucion (bool) y si tiene forma gigamax (bool)
# para el cual debemos construir tres árboles para acceder de manera eficiente a los datos contemplando lo siguiente:
# los índices de cada uno de los árboles deben ser nombre, número y tipo;

#A mostrar todos los datos de un Pokémon a partir de su número y nombre –para este último, la búsqueda debe ser por proximidad,
# es decir si busco “bul” se deben mostrar todos los Pokémons cuyos nombres comiencen o contengan dichos caracteres–;

#B mostrar todos los nombres de los Pokémons de un determinado tipo: fantasma, fuego, acero y eléctrico;
# realizar un listado en orden ascendente por número y nombre de Pokémon, y además un listado por nivel por nombre;

#C mostrar todos los Pokémons que son débiles frente a Jolteon, Lycanroc y Tyrantrum;

#D mostrar todos los tipos de Pokémons y cuántos hay de cada tipo;

#E determinar cuantos Pokémons tienen megaevolucion.

#F determinar cuantos Pokémons tiene forma gigamax.

#G cargue al menos 100 Pokémons.

import json

from Arboles import Pokemon, crear_arbol_nombre, crear_arbol_numero, crear_arbol_tipo

#leer el json y crear los objetos Pokemon

def cargar_pokemons_desde_json(ruta_archivo):
    """Lee el archivo json y devuelve una lista de objetos Pokemon."""
    lista_pokemons = []

    with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
        datos_json = json.load(archivo)

    for item in datos_json:
        p = Pokemon(
            nombre=item['nombre'],
            numero=item['numero'],
            tipos=item['tipos'],
            debilidades=item['debilidades'],
            mega_evolucion=item['mega_evolucion'],
            gigamax=item['gigamax']
        )
        lista_pokemons.append(p)

    return lista_pokemons


# --- CORRECCIÓN: Cargamos los datos antes de usarlos ---
lista_pokemons = cargar_pokemons_desde_json("pokemons.json")


# PUNTO A: Construcción de los 3 árboles y verificación de índices

print("\n Construyendo los 3 árboles (Índices: Nombre, Número, Tipo) ")
arbol_nombre = crear_arbol_nombre(lista_pokemons)

arbol_numero = crear_arbol_numero(lista_pokemons)

arbol_tipo = crear_arbol_tipo(lista_pokemons)
print("¡Árboles creados con éxito!")

print("\nVerificación Árbol  por NOMBRE (Primeros 5):")

def mostrar_primeros_nombre(root, contador=[0]):
    if root is not None and contador[0] < 5:
        mostrar_primeros_nombre(root.left, contador)
        if contador[0] < 5:
            print(f"  {root.value}")
            contador[0] += 1
        mostrar_primeros_nombre(root.right, contador)
mostrar_primeros_nombre(arbol_nombre.root)

print("\nVerificación Árbol  NÚMERO (Primeros 5):")


def mostrar_primeros_numero(root, contador=[0]):
    if root is not None and contador[0] < 5:
        mostrar_primeros_numero(root.left, contador)
        if contador[0] < 5:
            print(f"  {root.value} - {root.other_values.nombre}")
            contador[0] += 1
        mostrar_primeros_numero(root.right, contador)
mostrar_primeros_numero(arbol_numero.root)

print("\nVerificación Árbol por TIPO (Primeros 5):")


def mostrar_primeros_tipo(root, contador=[0]):
    if root is not None and contador[0] < 5:
        mostrar_primeros_tipo(root.left, contador)
        if contador[0] < 5:
            print(f"  {root.value} - {root.other_values.nombre}")
            contador[0] += 1
        mostrar_primeros_tipo(root.right, contador)
mostrar_primeros_tipo(arbol_tipo.root)

# PUNTO B: Búsqueda por número exacto, por nombre (proximidad) y listados

print("\n b. Búsqueda por Número (Ej: 6) ")
numero_a_buscar = 6
nodo_encontrado = arbol_numero.search(numero_a_buscar)

if nodo_encontrado is not None:
    print(nodo_encontrado.other_values)
else:
    print(f"No se encontró ningún Pokémon con el número {numero_a_buscar}.")

print("\n b. Búsqueda por Nombre (Ej: 'char') ")

def buscar_por_proximidad(arbol, subcadena):
    def __recorrer(root, subcadena):
        if root is not None:
            __recorrer(root.left, subcadena)
            if subcadena.lower() in str(root.value).lower():
                print(root.other_values)
            __recorrer(root.right, subcadena)
    __recorrer(arbol.root, subcadena)

buscar_por_proximidad(arbol_nombre, "char")


print("--- Mostrando nombres filtrados por su clave TIPO ---")

def mostrar_por_tipo(arbol, tipo_buscado):
    def __inorden(root, tipo_buscado):
        if root is not None:
            __inorden(root.left, tipo_buscado)
            if str(root.value).lower() == tipo_buscado.lower():
                print(f"  - {root.other_values.nombre}")
            __inorden(root.right, tipo_buscado)
    __inorden(arbol.root, tipo_buscado)

tipos_a_buscar = ["Fantasma", "Fuego", "Acero", "Eléctrico"]
for tipo in tipos_a_buscar:
    print(f"\nTipo '{tipo}':")
    mostrar_por_tipo(arbol_tipo, tipo)


print("\n b. Listado ascendente por NÚMERO ")

def mostrar_inorden_con_nombre(root):
    if root is not None:
        mostrar_inorden_con_nombre(root.left)
        print(f"  {root.value} - {root.other_values.nombre}")
        mostrar_inorden_con_nombre(root.right)

mostrar_inorden_con_nombre(arbol_numero.root)
print("----------------------------------")

print("\n b. Listado ascendente por NOMBRE ")

arbol_nombre.inorden()
print("----------------------------------")

print("\n b. Listado por NIVEL por NOMBRE ")

arbol_nombre.by_level()
print("----------------------------------")


# PUNTO C: Mostrar Pokémons débiles frente a Jolteon, Lycanroc o Tyrantrum


print("\n c. Pokémons débiles frente a Jolteon, Lycanroc o Tyrantrum ")

def buscar_debiles(arbol):
    """Recorre el árbol y muestra los Pokémons que sean débiles frente a AL MENOS UNO de los 3."""
    resultados = set()
    debilidades_buscadas = ["Jolteon", "Lycanroc", "Tyrantrum"]
    
    def __inorden(root):
        if root is not None:
            __inorden(root.left)
            
            p = root.other_values
            es_debil = False
            
            # Recorremos las debilidades buscadas
            for debilidad in debilidades_buscadas:
                # Si la debilidad está en la lista de debilidades del Pokémon
                if debilidad in p.debilidades:
                    es_debil = True
                    break # Con encontrar una sola, ya alcanza
                    
            if es_debil:
                resultados.add(str(p))
                
            __inorden(root.right)
            
    __inorden(arbol.root)
    
    if resultados:
        for p in sorted(resultados):
            print(f"  - {p}")
    else:
        print("  No se encontraron Pokémons con esas debilidades.")

buscar_debiles(arbol_nombre)

# PUNTO D: Mostrar todos los tipos de Pokémons y cuántos hay de cada tipo

print("\n d. Tipos de Pokémons y cantidad de cada tipo ")

def contar_tipos(arbol):
    """Recorre el árbol de tipos y cuenta cuántas veces aparece cada uno."""
    conteo = {}
    
    def __inorden(root):
        if root is not None:
            __inorden(root.left)
            
            tipo = str(root.value) # El tipo (clave del nodo)
            if tipo in conteo:
                conteo[tipo] += 1
            else:
                conteo[tipo] = 1
                
            __inorden(root.right)
            
    __inorden(arbol.root)
    return conteo

conteo_tipos = contar_tipos(arbol_tipo)

# Mostramos los resultados ordenados alfabéticamente por tipo
for tipo, cantidad in sorted(conteo_tipos.items()):
    print(f"  - {tipo}: {cantidad}")

    # PUNTO E: Determinar cuántos Pokémons tienen Mega Evolución

print("\n e. Determinando cuántos Pokémons tienen Mega Evolución ")

def contar_mega(arbol):
    """Recorre el árbol y cuenta cuántos tienen mega evolución."""
    conteo = 0
    
    def __inorden(root):
        nonlocal conteo
        if root is not None:
            __inorden(root.left)
            if root.other_values.mega_evolucion:
                conteo += 1
            __inorden(root.right)
            
    __inorden(arbol.root)
    return conteo

total_mega = contar_mega(arbol_nombre)
print(f"  Total con Mega Evolución: {total_mega}")

# PUNTO F: Determinar cuántos Pokémons tienen forma Gigamax

print("\n f. Determinando cuántos Pokémons tienen forma Gigamax ")

def contar_gigamax(arbol):
    """Recorre el árbol y cuenta cuántos tienen forma Gigamax."""
    conteo = 0
    
    def __inorden(root):
        nonlocal conteo
        if root is not None:
            __inorden(root.left)
            if root.other_values.gigamax:
                conteo += 1
            __inorden(root.right)
            
    __inorden(arbol.root)
    return conteo

total_gigamax = contar_gigamax(arbol_nombre)
print(f"  Total con Forma Gigamax: {total_gigamax}")

# PUNTO G: Verificar cantidad total de Pokémons y nodos en cada árbol

print("\n g. Verificando cantidad total de Pokémons y nodos en cada árbol ")

def contar_nodos(root):
    """Recorre el árbol en inorden y cuenta cuántos nodos tiene."""
    if root is None:
        return 0
    return 1 + contar_nodos(root.left) + contar_nodos(root.right)

total_pokemons = len(lista_pokemons)

if total_pokemons >= 100:
    print(f"\n  ¡Éxito! Se cargaron {total_pokemons} Pokémons desde el JSON (cumple con el mínimo de 100).")
else:
    print(f"  Atención: Solo se cargaron {total_pokemons} Pokémons (el mínimo requerido es 100).")

print(f"\n  Cantidad de nodos en el Árbol por NOMBRE: {contar_nodos(arbol_nombre.root)}")
print(f"  Cantidad de nodos en el Árbol por NÚMERO: {contar_nodos(arbol_numero.root)}")
print(f"  Cantidad de nodos en el Árbol por TIPO:   {contar_nodos(arbol_tipo.root)}")
print(" \n (Nota: el Árbol por TIPO tiene más nodos porque un Pokémon con 2 tipos se inserta 2 veces).")
