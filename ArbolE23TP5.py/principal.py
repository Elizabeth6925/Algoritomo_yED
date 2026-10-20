# 23. Implementar un algoritmo que permita generar un árbol con los datos de la siguiente tabla y
# resuelva las siguientes consultas:
# a. listado inorden de las criaturas y quienes la derrotaron;
# b. se debe permitir cargar una breve descripción sobre cada criatura;
# c. mostrar toda la información de la criatura Talos;
# d. determinar los 3 héroes o dioses que derrotaron mayor cantidad de criaturas;
# e. listar las criaturas derrotadas por Heracles;
# f. listar las criaturas que no han sido derrotadas;
# g. además cada nodo debe tener un campo “capturada” que almacenará el nombre del héroe
# o dios que la capturo;
# h. modifique los nodos de las criaturas Cerbero, Toro de Creta, Cierva Cerinea y Jabalí de
# Erimanto indicando que Heracles las atrapó;
# i. se debe permitir búsquedas por coincidencia;
# j. eliminar al Basilisco y a las Sirenas;
# k. modificar el nodo que contiene a las Aves del Estínfalo, agregando que Heracles
# derroto a varias;
# l. modifique el nombre de la criatura Ladón por Dragón Ladón;
# m. realizar un listado por nivel del árbol;
# n. muestre las criaturas capturadas por Heracles.


from criaturasdata import CRIATURAS_DATA
from genArbol import ArbolBinario


if __name__ == "__main__":
    # 1. Crear el árbol vacío
    arbol = ArbolBinario()

    # 2. Insertar todas las criaturas en el árbol
    for nombre, derrotado_por in CRIATURAS_DATA:
        arbol.insertar(nombre, derrotado_por)

    # punto a : Mostrar el recorrido inorden

    print("Listado inorden de criaturas:")
    arbol.recorrido_inorden(arbol.raiz)




# punto b : Descrpcion de cada criatura

    print("\nDescripción de cada criatura:")
    for nombre, _ in CRIATURAS_DATA:
        descripcion = input(f"Ingrese una breve descripción para {nombre}: ")
        arbol.agregar_descripcion(nombre, descripcion)
