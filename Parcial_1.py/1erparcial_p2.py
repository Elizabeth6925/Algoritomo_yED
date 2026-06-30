#Ejercicio 1: Dado una lista simple de python (array) de 15 superheroes realizar dos funciones recursivas:
#funcion recursiva  para buscar, determinar si Capitan America esta en la lista.
#funcion recursiva para listar los superheroes de la lista.

from lista_ import List, Heroe, by_name, by_real_name, by_first_appearance

from super_heroes_data import superheroes
 
from buscarCA import buscar_capitan
l = List()
l.add_criterion('name', by_name)
l.add_criterion('real_name', by_real_name)


for datos in superheroes[:15]:
    l.append(Heroe(
        name             = datos["name"],
        alias            = datos["alias"],
        real_name        = datos["real_name"],
        short_bio        = datos["short_bio"],
        first_appearance = datos["first_appearance"],
        is_villain       = datos["is_villain"]
    ))

l.show()
print(buscar_capitan(l))