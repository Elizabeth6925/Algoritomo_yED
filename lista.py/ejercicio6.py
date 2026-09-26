#Generar también otra lista de elementos aleatorios de distintos tamaños (100 000, 1 000 000, 10000 000),
# # para probar los distintos algoritmos de búsqueda vistos. Además agregar las instrucciones necesarias para medir su tiempo de ejecución 
# #para poder compararlos.

import random
import time

from crear_lista import crear_lista, cargar_lista, tamanio_aleatorio
from busqueda_lineal import busqueda_lineal
from busqueda_binaria import busqueda_binaria


def medir_tiempo(funcion, *args):
    inicio = time.perf_counter()
    resultado = funcion(*args)
    fin = time.perf_counter()
    return resultado, fin - inicio


def elegir_metodo():
    print("Métodos de búsqueda:")
    print("1. Lineal")
    print("2. Binaria")
    print("3. Ambos")
    opcion = input("Elegí una opción: ")
    return opcion


# def mostrar_en_columnas(lista, columnas=4):
#     ancho = max(len(str(elemento)) for elemento in lista) + 2
#     for i in range(0, len(lista), columnas):
#         fila = lista[i:i + columnas]
#         print(''.join(str(elemento).ljust(ancho) for elemento in fila))


opcion = elegir_metodo()
tamanio = tamanio_aleatorio()

lista = crear_lista()
cargar_lista(lista, tamanio)

print("Elementos:")
print(f"la lista puede contener personajes de Marvel, Harry Potter, hadas de Disney, planetas y estrellas, eventos históricos y personajes de Avatar: La Leyenda de Aang.")
# mostrar_en_columnas(lista)
#print(f"Tamaño de la lista: {len(lista)}")
#print(f"Tiempo de carga de la lista: {tamanio:.6f} s")
valor_buscado = input("Ingresá el elemento a buscar: ")

if opcion in ('1', '3'):
    posicion, tiempo_lineal = medir_tiempo(busqueda_lineal, lista, valor_buscado)
    if posicion != -1:
        print(f"  Búsqueda lineal: encontrado en la posición {posicion} ({tiempo_lineal:.6f} s)")
    else:
        print(f"  Búsqueda lineal: no encontrado ({tiempo_lineal:.6f} s)")

if opcion in ('2', '3'):
    lista_ordenada = sorted(lista, key=str.lower)
    posicion, tiempo_binaria = medir_tiempo(busqueda_binaria, lista_ordenada, valor_buscado)
    if posicion != -1:
        print(f"  Búsqueda binaria: encontrado en la posición {posicion} ({tiempo_binaria:.6f} s)")
    else:
        print(f"  Búsqueda binaria: no encontrado ({tiempo_binaria:.6f} s)")