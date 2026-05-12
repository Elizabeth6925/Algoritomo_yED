#24. Dada una pila de personajes de Marvel Cinematic Universe (MCU), de los cuales se dispone de
#su nombre y la cantidad de películas de la saga en la que participó, implementar las funciones
#necesarias para resolver las siguientes actividades:

#a. determinar en qué posición se encuentran Rocket Raccoon y Groot, 
# tomando como posición uno la cima de la pila;

#b. determinar los personajes que participaron en más de 5 películas de la saga,
#además indicar la cantidad de películas en la que aparece;

#c. determinar en cuantas películas participo la Viuda Negra (Black Widow);

#d. mostrar todos los personajes cuyos nombre empiezan con C, D y G


from pila_muc import crear_pila, esta_vacia, cima, desapilar, apilar    
from posicion import posiciones_rocket_groot
from personajes_masde_5p import personajes_mas_de_5_peliculas
from peliculas_bw import peliculas_black_widow
from comienza_con_ import nombres_con_CDG

def main():
    pila = crear_pila()

    print("a. Posiciones de Rocket Raccoon y Groot:")
    posiciones_rocket_groot(pila)

    print("\nb. Personajes que participaron en más de 5 películas:")
    personajes = personajes_mas_de_5_peliculas(pila)
    for nombre, peliculas in personajes:
        print(f"{nombre}: {peliculas} películas")

    print("\nc. Cantidad de películas en las que participó la Viuda Negra:")
    peliculas_bw = peliculas_black_widow(pila)
    print(f"Viuda Negra participó en {peliculas_bw} películas")

    print("\nd. Personajes cuyos nombres empiezan con C, D y G:")
    nombres_con_CDG(pila)

if __name__ == "__main__":
    main()      