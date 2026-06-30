#Poner todos los villanos en una cola para determinar luego cuales aparecieron antes de 1980.

from cola import Queue

def villanos_a_cola(lista, indice: int = 0, villanos: list = None) -> Queue:
    if villanos is None:
        villanos = []
    if indice >= len(lista):
        print("\nVillanos:")
        cola = Queue()
        for villano in villanos:
            print(villano)
            cola.arrive(villano)
        return cola
    if lista[indice].is_villain:
        villanos.append(lista[indice])
    return villanos_a_cola(lista, indice + 1, villanos)
