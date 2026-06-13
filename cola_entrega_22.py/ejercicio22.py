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

from crear_cola_mcu import crear_cola, cargar_cola, mostrar_cola

def main():
    cola = cargar_cola()
    mostrar_cola(cola)
main()

