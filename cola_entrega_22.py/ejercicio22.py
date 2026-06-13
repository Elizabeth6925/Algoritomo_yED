#22. Se tienen una cola con personajes de Marvel Cinematic Universe (MCU), 
# de los cuales se conoce el nombre del personaje, el nombre del superhéroe y su género (Masculino M y FemeninoF)
# –por ejemplo {Tony Stark, Iron Man, M}, {Steve Rogers, Capitán América, M}, {Natasha Ro-manoff, Black Widow, F},
#  etc., desarrollar un algoritmo que resuelva las siguientes actividades:
# a. determinar el nombre del personaje de la superhéroe Capitana Marvel;
# b. mostrar los nombre de los superhéroes femeninos;
# c. mostrar los nombres de los personajes masculinos;
# d. determinar el nombre del superhéroe del personaje Scott Lang;
# e. mostrar todos datos de los superhéroes o personaje cuyos nombres comienzancon la letra S;
# f. determinar si el personaje Carol Danvers se encuentra en la cola e indicar su nombrede de superhéroes.

from crear_cola import crear_cola, desencolar, esta_vacia
from cargar_cola import carga_cola, mostrar_cola
from Cap_marvel import personaje_de_capitana_marvel
from genero import filtrar_por_genero 
from encontrar_scott import heroe_de_scott_lang
from comiensa_con_s import nombres_con_s
from encontrar_carol_danvers import encontrar_carol_danvers


print(f"\nCargando cola con personajes de Marvel Cinematic Universe...\n")

cola = carga_cola()
mostrar_cola(cola)  

print(f"\nEjercicio a: Determinar el nombre del personaje de la superhéroe Capitana Marvel")

personaje = personaje_de_capitana_marvel(cola)


print(f"\nEl personaje de la superhéroe Capitana Marvel es: {personaje}")


print(f"\nEjercicio b: Mostrar los nombre de los superhéroes femeninos\n") 

femeninos = filtrar_por_genero(cola, "F")

if esta_vacia (femeninos):
    
    print("\nNo hay superhéroes femeninos en la cola.\n") 
else:
    while not esta_vacia(femeninos):

        p = desencolar(femeninos)

        print(p["nombre_heroe"])


print(f"\nEjercicio c: Mostrar los nombres de los personajes masculinos\n")

masculinos = filtrar_por_genero(cola, "M")

if esta_vacia(masculinos):

    print("\nNo hay personajes masculinos en la cola.\n")

else:
    while not esta_vacia(masculinos):

     p = desencolar(masculinos)

     print(p["nombre_real"])


print(f"\nEjercicio d: Determinar el nombre del superhéroe del personaje Scott Lang\n")

heroe = heroe_de_scott_lang(cola)

if heroe is None:
    print("No se puede determinar el nombre de su superhéroe porque Scott Lang no figura en la lista.")
else:
    print(f"El superhéroe de Scott Lang es: {heroe}\n")


print(f"\nEjercicio e: Mostrar todos datos de los superhéroes o personaje cuyos nombres comienzan con la letra S\n")

print(f"\nEjercicio e: Mostrar todos los datos de los superhéroes o personajes cuyos nombres comienzan con la letra S\n")

por_nombre_real, por_nombre_heroe = nombres_con_s(cola)

print("Por nombre real:")
print(f"{'Nombre Real':<25} {'Héroe':<20} {'Género'}")

while not esta_vacia(por_nombre_real):
    p = desencolar(por_nombre_real)
    print(f"{p['nombre_real']:<25} {p['nombre_heroe']:<20} {p['genero']}")

print("\nPor nombre de superhéroe:")
print(f"{'Nombre Real':<25} {'Héroe':<20} {'Género'}")

while not esta_vacia(por_nombre_heroe):
    p = desencolar(por_nombre_heroe)
    print(f"{p['nombre_real']:<25} {p['nombre_heroe']:<20} {p['genero']}")

print(f"\nEjercicio f: Determinar si el personaje Carol Danvers se encuentra en la cola e indicar su nombre de superhéroes")

carol_heroe = encontrar_carol_danvers(cola)

if carol_heroe is None:
    print("\nCarol Danvers no se encuentra en la cola.")
else:
    print(f"\nCarol Danvers se encuentra en la cola y su nombre de superhéroe es: {carol_heroe}")

