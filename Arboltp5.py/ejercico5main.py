# 5. Dado un árbol con los nombre de los superhéroes y villanos de la saga Marvel Cinematic Univer-
# se (MCU), desarrollar un algoritmo que contemple lo siguiente:

# a. además del nombre del superhéroe, en cada nodo del árbol se almacenará un campo boo-
# leano que indica si es un héroe o un villano, True y False respectivamente;
# b. listar los villanos ordenados alfabéticamente;
# c. mostrar todos los superhéroes que empiezan con C;
# d. determinar cuántos superhéroes hay el árbol;
# e. Doctor Strange en realidad está mal cargado. Utilice una búsqueda por proximidad para
# encontrarlo en el árbol y modificar su nombre;
# f. listar los superhéroes ordenados de manera descendente;
# g. generar un bosque a partir de este árbol, un árbol debe contener a los superhéroes y otro a
# los villanos, luego resolver las siguiente tareas:
# I. determinar cuántos nodos tiene cada árbol;
# II. realizar un barrido ordenado alfabéticamente de cada árbol.

print("Iniciando el programa para procesar el árbol de superhéroes y villanos de la saga Marvel Cinematic Universe (MCU) y resolucion item a ")
from arbole5 import BinaryTree
from super_heroes_data import superheroes

# Creamos el árbol principal único
arbol_marvel = BinaryTree()

# Carga general: se insertan héroes y villanos juntos
for personaje in superheroes:
    arbol_marvel.insert_node(personaje['name'], other_value=personaje)
 
print("Carga general finalizada. El árbol ya contiene a todos los personajes con sus datos integrados.")   


#item b
print("\n--- Villanos ordenados alfabéticamente ---")

from listas import listar_villanos_alfabeticamente

print("\n--- Villanos ordenados alfabéticamente ---")
listar_villanos_alfabeticamente(arbol_marvel.root)

#item c
print("\n--- Superhéroes que empiezan con 'C' ---")

from listas import listar_heroes_con_c  

print("\n--- Superhéroes que empiezan con 'C' ---")
listar_heroes_con_c(arbol_marvel.root)

# item f 
print("\n--- Superhéroes ordenados de manera descendente ---")

from listas import listar_heroes_descendente 

print("\n--- Superhéroes ordenados de manera descendente ---")
listar_heroes_descendente(arbol_marvel.root)

# item d
print("\n--- Contando superhéroes en el árbol ---")

from contar import contar_heroes

total_heroes = contar_heroes(arbol_marvel.root)
print(f"\n--- Cantidad de superhéroes en el árbol ---")
print(f"Total de héroes: {total_heroes}")

#item e
print("\n--- Modificando el nombre de Doctor Strange ---")

from buscar import modificar_doctor_strange_proximidad

# Le pasamos el árbol completo para que pueda eliminar e reinsertar
modificar_doctor_strange_proximidad(arbol_marvel, nuevo_nombre="Dr Strange")

# item g
print("\n--- Generando bosque de héroes y villanos ---")

from bosque import generar_bosque
from contar import contar_nodos

# Creamos los árboles para el bosque
arbol_heroes = BinaryTree()
arbol_villanos = BinaryTree()

# Generamos el bosque
generar_bosque(arbol_marvel.root, arbol_heroes, arbol_villanos)

# Para los árboles del bosque (ítem g)
total_heroes = contar_nodos(arbol_heroes.root)
total_villanos = contar_nodos(arbol_villanos.root)

print(f"\n--- Cantidad de nodos en el árbol de héroes ---")
print(f"Total de héroes: {total_heroes}")
print(f"\n--- Cantidad de nodos en el árbol de villanos ---")
print(f"Total de villanos: {total_villanos}")
