#Ejercicio 2: Dada una lista de personajes de marvel (usar el archivo adjunto) debe tener 100 o mas, resolver:
#Listado ordenado de manera ascendente por nombre de los personajes.
#Determinar en que posicion esta The Thing y Rocket Raccoon.
#Poner todos los villanos en una cola para determinar luego cuales aparecieron antes de 1980.
#Listar los superheores que comienzan con  Bl, G, My, y W.
#Listado de personajes ordenado por nombre real de manera ascendente de los personajes.
#Listado de superheroes ordenados por fecha de aparación.
#Modificar el nombre real de Ant Man a Scott Lang.
#Mostrar los personajes que en su biografia incluyan la palabra time-traveling o suit.
#Eliminar a Electro y Baron Zemo de la lista y mostrar su información si estaba en la lista.
#Importante una vez terminado el parcial subirlo a github y pegar el link en la entrega.



from lista_mas100 import List, Heroe, by_name, by_real_name, by_first_appearance
from super_heroes_data import superheroes
from cola import Queue
from filtrar_prefijos import filtrar_prefijos
from filtrar_bio import filtrar_bio
from eliminar_heroes import eliminar_heroe
from buscar_pos import buscar_posicion
 
l = List()
l.add_criterion('name', by_name)
l.add_criterion('real_name', by_real_name)
l.add_criterion('first_appearance', by_first_appearance)
 
for datos in superheroes:
    l.append(Heroe(
        name             = datos["name"],
        alias            = datos["alias"],
        real_name        = datos["real_name"],
        short_bio        = datos["short_bio"],
        first_appearance = datos["first_appearance"],
        is_villain       = datos["is_villain"]
    ))
 
 
print("\n Listado ordenado por nombre ")
l.sort_by_criterion('name')
l.show()
 
 
print("\n Posición de The Thing y Rocket Raccoon ")
print(buscar_posicion(l, "The Thing"))
print(buscar_posicion(l, "Rocket Raccoon"))
 
 
print("\n Villanos ")
cola_villanos = Queue()
for heroe in l:
    if heroe.is_villain:
        print(heroe)
        cola_villanos.arrive(heroe)
 

print("\n Villanos anteriores a 1980")
for _ in range(cola_villanos.size()):
    villano = cola_villanos.attention()
    if villano.first_appearance < 1980:
        print(villano)
 
 

print("\nSuperhéroes que empiezan con Bl, G, My, W")

filtrar_prefijos(l, ("Bl", "G", "My", "W"))
 
 

print("\nListado ordenado por nombre real")
l.sort_by_criterion('real_name')
l.show()
 
 


print("\nListado ordenado por fecha de aparición ")
l.sort_by_criterion('first_appearance')
l.show()
 
 
print("\n Modificar nombre real de Ant Man a Scott Lang")
for heroe in l:
    if heroe.name == "Ant Man":
        heroe.real_name = "Scott Lang"
        print(heroe)
 
 

print("\nPersonajes con 'time-traveling' o 'suit' en su biografía ")
filtrar_bio(l, ["time-traveling", "suit"])
 
 


print("\n Eliminar Electro y Baron Zemo ")

for nombre in ["Electro", "Baron Zemo"]:

    eliminado = eliminar_heroe(l, nombre)
    if eliminado:
        print(f"Eliminado: {eliminado}")
    else:
        print(f"{nombre} no estaba en la lista")
 