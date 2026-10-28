# 23. Implementar un algoritmo que permita generar un árbol con los datos de la siguiente tabla y
# resuelva las siguientes consultas:
# a. listado inorden de las criaturas y quienes la derrotaron;
# b. se debe permitir cargar una breve descripción sobre cada criatura;
# c. mostrar toda la información de la criatura Talos;
# d. determinar los 3 héroes o dioses que derrotaron mayor cantidad de criaturas;
# e. listar las criaturas derrotadas por Heracles;
# f. listar las criaturas que no han sido derrotadas;
# g. además cada nodo debe tener un campo "capturada" que almacenará el nombre del héroe
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
from genArbol import ArbolBinario, busqueda_coincidencia
from contar import contar_derrotas


if __name__ == "__main__":
    # 1. Crear el árbol vacío
    arbol = ArbolBinario()

    # 2. Insertar todas las criaturas en el árbol
    for nombre, derrotado_por in CRIATURAS_DATA:
        arbol.insertar(nombre, derrotado_por)

    # =========================================================
    # a. Mostrar el recorrido inorden
    # =========================================================
    print("Listado inorden de criaturas:")
    arbol.recorrido_inorden(arbol.raiz)

    # =========================================================
    # b. Descripción de cada criatura
    # =========================================================
    print("\nDescripción de cada criatura:")
    for nombre, _ in CRIATURAS_DATA:
        descripcion = input(f"Ingrese una breve descripción para {nombre}: ")
        arbol.agregar_descripcion(nombre, descripcion)

    print("\n--- LISTADO COMPLETO ---")
    arbol.recorrido_inorden(arbol.raiz)

    # =========================================================
    # c. Mostrar toda la información de la criatura Talos
    # =========================================================
    if arbol.buscar("Talos"):
        print("\nInformación de la criatura Talos:")
        arbol.mostrar_informacion("Talos")
    else:
        print("\nLa criatura Talos no se encuentra en el árbol.")

    # =========================================================
    # k. Modificar Aves del Estínfalo: Heracles derrotó a varias
    # (se hace antes del d para que cuente en el top 3)
    # =========================================================
    arbol.agregar_nota("Aves del Estínfalo", "Heracles derrotó a varias de estas aves.")
    print("\nInformación de las Aves del Estínfalo después de la modificación:")
    arbol.mostrar_informacion("Aves del Estínfalo")

    # =========================================================
    # d. Determinar los 3 héroes o dioses que derrotaron más criaturas
    # =========================================================
    print("\nLos 3 héroes o dioses que derrotaron mayor cantidad de criaturas:")
    derrotas = {}
    contar_derrotas(arbol.raiz, derrotas)
    top3 = sorted(derrotas.items(), key=lambda x: x[1], reverse=True)[:3]
    for heroe, cantidad in top3:
        print(f"{heroe}: {cantidad} criaturas")

    # =========================================================
    # e. Listar las criaturas derrotadas por Heracles
    # =========================================================
    print("\nCriaturas derrotadas por Heracles:")

    def listar_criaturas_derrotadas_por(nodo, heroe):
        if nodo is not None:
            listar_criaturas_derrotadas_por(nodo.izq, heroe)
            if nodo.derrotado_por == heroe:
                print(f"- {nodo.nombre}")
            listar_criaturas_derrotadas_por(nodo.der, heroe)

    listar_criaturas_derrotadas_por(arbol.raiz, "Heracles")

    # =========================================================
    # f. Listar las criaturas que no han sido derrotadas
    # =========================================================
    print("\nCriaturas que no han sido derrotadas:")

    def listar_criaturas_no_derrotadas(nodo):
        if nodo is not None:
            listar_criaturas_no_derrotadas(nodo.izq)
            if nodo.derrotado_por is None:
                print(f"- {nodo.nombre}")
            listar_criaturas_no_derrotadas(nodo.der)

    listar_criaturas_no_derrotadas(arbol.raiz)

    # =========================================================
    # h. Marcar capturas de Heracles
    # =========================================================
    criaturas_capturadas = [
        "Cerbero",
        "Toro de Creta",
        "Cierva de Cerinea",
        "Jabalí de Erimanto",
    ]
    for criatura in criaturas_capturadas:
        ok = arbol.asignar_captura(criatura, "Heracles")
        if not ok:
            print(f"  No se encontró '{criatura}'")

    # =========================================================
    # n. Mostrar las criaturas capturadas por Heracles
    # =========================================================
    arbol.criaturas_capturadas_por("Heracles")

    # =========================================================
    # i. Búsqueda por coincidencia
    # =========================================================
    busqueda = input("\nIngrese una subcadena para buscar criaturas: ")
    if busqueda.strip():
        resultados = busqueda_coincidencia(arbol.raiz, busqueda)
        print(f"\nResultados para '{busqueda}':")
        if resultados:
            for criatura in resultados:
                print(f"- {criatura.nombre}")
        else:
            print("(sin resultados)")
    else:
        print("\nBúsqueda vacía: no se busca nada.")

    # =========================================================
    # j. Eliminar al Basilisco y a las Sirenas
    # =========================================================
    arbol.eliminar_criatura("Basilisco")
    arbol.eliminar_criatura("Sirenas")

    print("\nListado inorden después de eliminar Basilisco y Sirenas:")
    arbol.recorrido_inorden(arbol.raiz)

    # =========================================================
    # l. Renombrar Ladón -> Dragón Ladón
    # =========================================================
    if arbol.renombrar("Ladón", "Dragón Ladón"):
        print("\nLadón renombrado a 'Dragón Ladón' correctamente.")
        print("\nInformación del Dragón Ladón:")
        arbol.mostrar_informacion("Dragón Ladón")
    else:
        print("\nNo se encontró 'Ladón'.")

    # =========================================================
    # m. Listado por nivel del árbol
    # =========================================================
    print("\nListado por nivel del árbol:")
    arbol.listado_por_nivel()