#El problema de la mochila Jedi. Suponga que un Jedi (Luke Skywalker, Obi-Wan Kenobi, Rey u
#otro, el que más le guste) está atrapado, pero muy cerca está su mochila que contiene muchos
#objetos. Implementar una función recursiva llamada “usar la fuerza” que le permita al Jedi “con
#ayuda de la fuerza” realizar las siguientes actividades:

# a. sacar los objetos de la mochila de a uno a la vez hasta encontrar un sable de luz o que no queden más objetos en la mochila;

#b. determinar si la mochila contiene un sable de luz y cuantos objetos fueron necesarios sacar para encontrarlo;

#c. Utilizar un vector para representar la mochila.

def usar_la_fuerza(mochila, indice=0, contador=0):

    # Caso base: fin de la lista
    if indice >= len(mochila):
        return False, contador

    objeto = mochila[indice].strip().lower() # limpia espacios
    contador += 1

    print(f"Revisando: '{objeto}'")  # para ver qué compara

    
    if "sable de luz" in objeto:
        return True, contador

    return usar_la_fuerza(mochila, indice + 1, contador)

# CARGA VECTOR

mochila = []

n = int(input("¿Cuántos objetos tiene la mochila?: "))

for i in range(n):
    obj = input(f"Ingrese el objeto {i+1}: ").lower()
    mochila.append(obj)

# PROCESO RECURSIVO

encontrado, cantidad = usar_la_fuerza(mochila)

# RESULTADO

if encontrado:
    print(f"Se encontró el sable de luz después de sacar {cantidad} objetos.")
else:
    print(f"No se encontró el sable de luz. Se revisaron {cantidad} objetos.")