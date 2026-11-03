# Ejercicio 1: Se tiene los datos de Pokémons de las 9 generaciones cargados de manera aleatoria (1025 en total) de los cuales se conoce su nombre,
#  número, tipo/tipos, debilidad frente a tipo/tipos, si tiene mega evolucion (bool) y si tiene forma gigamax (bool) 
# para el cual debemos construir tres árboles para acceder de manera eficiente a los datos contemplando lo siguiente:

from tree import BinaryTree, Node


# CLASE POKEMON 


class Pokemon:
    def __init__(self, nombre, numero, tipos, debilidades, mega_evolucion, gigamax):
        self.nombre = nombre
        self.numero = numero
        self.tipos = tipos              # Lista: ["Planta", "Veneno"]
        self.debilidades = debilidades  # Lista: ["Fuego", "Psíquico"]
        self.mega_evolucion = mega_evolucion
        self.gigamax = gigamax

    def __str__(self):
        tipos_str = "/".join(self.tipos)
        deb_str = "/".join(self.debilidades)
        return f"#{self.numero:03d} - {self.nombre} | Tipos: {tipos_str} | Débil vs: {deb_str} | Mega: {self.mega_evolucion} | Giga: {self.gigamax}"



# CONSTRUCTOR DEL ÁRBOL 1 nombre 


def crear_arbol_nombre(lista_pokemons):
    """
    Recibe una lista de objetos Pokemon y devuelve un BinaryTree
    indexado por el nombre del Pokémon (orden alfabético).
    """
    arbol = BinaryTree()
    for p in lista_pokemons:
        # Clave: nombre | Dato extra: objeto Pokemon completo
        arbol.insert_node(p.nombre, p)
    return arbol


# CONSTRUCTOR DEL ÁRBOL 2 numero 


def crear_arbol_numero(lista_pokemons):
    """
    Recibe una lista de objetos Pokemon y devuelve un BinaryTree
    indexado por el número del Pokémon (orden numérico).
    """
    arbol = BinaryTree()
    for p in lista_pokemons:
        
        arbol.insert_node(p.numero, p)
    return arbol



# CONSTRUCTOR DEL ÁRBOL 3 tipos


def crear_arbol_tipo(lista_pokemons):
    """
    Recibe una lista de objetos Pokemon y devuelve un BinaryTree
    indexado por el tipo del Pokémon. 
    IMPORTANTE: Si un Pokémon tiene más de un tipo, se inserta varias 
    veces (una por cada tipo), para poder buscarlo por cualquiera de ellos.
    """
    arbol = BinaryTree()
    for p in lista_pokemons:
        for t in p.tipos:
            # Clave: tipo (string) | Dato extra: objeto Pokemon completo
            arbol.insert_node(t, p)
    return arbol