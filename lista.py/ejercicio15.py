# 15. Se cuenta con una lista de canciones, de cada una de estas conocemos su nombre, nombre de la
# bandas o artista, y el año de lanzamiento del álbum; desarrollar las funciones necesarias para
# dar solución a las siguientes tareas:
# a. realizar un listado ordenado por canción, por banda o artista y por año de lanzamiento,
# utilizando el método que sea más optimo para cada tipo de dato;
# b. determinar si en la lista existe alguna canción de Audioslave y Rolling Stone;
# c. mostrar todas las canciones de Nirvana;
# d. agregar una nueva canción a la lista, y volver a realizar un listado ordenado por nombre de canción;
# e. determinar cuantas canciones de los Red Hot Chili Peppers hay en la lista;
# f. mostrar toda la información de las canciones “Fake tales of San Francisco” y “Black hole sun”.

from cear_list import obtener_lista_canciones
from ordenar import ordenar_por_criterio, quicksort_por_campo
from busquedas import existe_artista, obtener_canciones_por_artista, contar_canciones_por_artista
from agregar_cancion import agregar_y_reordenar
from Info_canciones import busqueda_binaria_cancion


def imprimir_tabla(titulo, lista):
    print(f"\n--- {titulo} ---")
    for pos, c in enumerate(lista, 1):
        print(f" {pos:02d}. '{c['cancion']}' - {c['artista']} ({c['anio']})")


def mostrar_menu():
    print("\n" + "="*60)
    print("        SISTEMA DE GESTIÓN DE CANCIONES - EJERCICIO 15")
    print("="*60)
    print("1. [Item A] Ordenar canciones (Seleccionar criterio)")
    print("2. [Item B] Verificar si existen canciones de Audioslave y Rolling Stones")
    print("3. [Item C] Mostrar todas las canciones de Nirvana")
    print("4. [Item D] Agregar una nueva canción y reordenar por nombre")
    print("5. [Item E] Contar cuántas canciones hay de Red Hot Chili Peppers")
    print("6. [Item F] Buscar información de canciones “Fake tales of San Francisco” y “Black hole sun” (Búsqueda Binaria)")
    print("7. Mostrar la lista base actual de canciones")
    print("0. Salir")
    print("="*60)


def main():
    canciones = obtener_lista_canciones()
    print("="*60)
    print("                  BASE DE DATOS INICIAL")
    print("="*60)
    imprimir_tabla(f"Lista cargada inicialmente ({len(canciones)} canciones)", canciones)

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (0-7): ").strip()

        if opcion == "1":
            print("\n>>> ITEM A: SELECCIÓN DE CRITERIO DE ORDENAMIENTO <<<")
            print("a. Ordenar por Nombre de Canción (Quicksort)")
            print("b. Ordenar por Banda o Artista (Quicksort)")
            print("c. Ordenar por Año de Lanzamiento (Counting Sort)")
            
            sub_opcion = input("Elija el criterio de ordenamiento (a/b/c): ").strip().lower()
            
            mapa_opciones = {"a": "1", "b": "2", "c": "3"}
            criterio = mapa_opciones.get(sub_opcion)

            if criterio:
                lista_ordenada, descripcion = ordenar_por_criterio(canciones, criterio)
                imprimir_tabla(f"Resultado del Ordenamiento por {descripcion}", lista_ordenada)
            else:
                print("\n[ERROR] Criterio de ordenamiento no válido.")

        elif opcion == "2":
            print("\n>>> EJECUTANDO ITEM B: VERIFICAR ARTISTAS <<<")
            for artista in ["Audioslave", "Rolling Stones"]:
                existe = existe_artista(canciones, artista)
                print(f"• ¿Existe alguna canción de {artista} en la lista?: {'Sí' if existe else 'No'}")

        elif opcion == "3":
            print("\n>>> EJECUTANDO ITEM C: MOSTRAR CANCIONES DE NIRVANA <<<")
            canciones_nirvana = obtener_canciones_por_artista(canciones, "Nirvana")
            imprimir_tabla("Canciones de Nirvana", canciones_nirvana)

        elif opcion == "4":
            print("\n>>> ITEM D: INGRESO DE NUEVA CANCIÓN <<<")
            print("Por favor, ingrese los datos de la canción que desea añadir:")
            
            nombre_input = input("  • Nombre de la canción: ").strip()
            artista_input = input("  • Banda o artista: ").strip()
            
            # Validación del año ingresado
            while True:
                anio_input = input("  • Año de lanzamiento: ").strip()
                if anio_input.isdigit() and len(anio_input) == 4:
                    anio_num = int(anio_input)
                    break
                print("    [!] Error: Ingrese un año válido (número de 4 dígitos).")

            if nombre_input and artista_input:
                canciones, lista_reordenada = agregar_y_reordenar(
                    canciones, nombre_input, artista_input, anio_num
                )
                print(f"\n[SISTEMA] ¡'{nombre_input}' fue agregada con éxito!")
                imprimir_tabla("Lista Reordenada por Nombre tras la incorporación", lista_reordenada)
            else:
                print("\n[ERROR] El nombre y el artista no pueden estar vacíos.")

        elif opcion == "5":
            print("\n>>> EJECUTANDO ITEM E: CONTAR CANCIONES DE RHCP <<<")
            total = contar_canciones_por_artista(canciones, "Red Hot Chili Peppers")
            print(f"• Cantidad total de canciones de Red Hot Chili Peppers: {total}")

        elif opcion == "6":
            print("\n>>> EJECUTANDO ITEM F: BÚSQUEDA BINARIA <<<")
            print("[INFO] Ordenando previamente la lista por nombre de canción para habilitar búsqueda binaria...")
            lista_para_binaria = quicksort_por_campo(canciones, "cancion")

            canciones_a_buscar = ["Fake Tales of San Francisco", "Black Hole Sun"]
            for cancion in canciones_a_buscar:
                resultado = busqueda_binaria_cancion(lista_para_binaria, cancion)
                if resultado:
                    print(f"• ENCONTRADA -> Canción: '{resultado['cancion']}' | Banda: {resultado['artista']} | Año: {resultado['anio']}")
                else:
                    print(f"• NOTA -> La canción '{cancion}' no fue encontrada.")

        elif opcion == "7":
            imprimir_tabla(f"Lista Base Actual ({len(canciones)} canciones)", canciones)

        elif opcion == "0":
            print("\n[SISTEMA] Saliendo del programa... ¡Hasta luego!\n")
            break

        else:
            print("\n[ERROR] Opción no válida. Por favor, ingrese un número del 0 al 7.")


if __name__ == "__main__":
    main()


#para ejecutar la vercion de agregar cancion donde el programa agrega una cancion aleatoria 
# from cear_list import obtener_lista_canciones
# from ordenar import ordenar_por_criterio, quicksort_por_campo
# from busquedas import existe_artista, obtener_canciones_por_artista, contar_canciones_por_artista
# from agregar_cancion import agregar_y_reordenar
# from Info_canciones import busqueda_binaria_cancion


# def imprimir_tabla(titulo, lista):
#     print(f"\n--- {titulo} ---")
#     for pos, c in enumerate(lista, 1):
#         print(f" {pos:02d}. '{c['cancion']}' - {c['artista']} ({c['anio']})")


# def mostrar_menu():
#     print("\n" + "="*60)
#     print("        SISTEMA DE GESTIÓN DE CANCIONES - EJERCICIO 15")
#     print("="*60)
#     print("1. [Item A] Ordenar canciones (Seleccionar criterio)")
#     print("2. [Item B] Verificar si existen canciones de Audioslave y Rolling Stones")
#     print("3. [Item C] Mostrar todas las canciones de Nirvana")
#     print("4. [Item D] Agregar una nueva canción y reordenar por nombre")
#     print("5. [Item E] Contar cuántas canciones hay de Red Hot Chili Peppers")
#     print("6. [Item F] Buscar información de canciones específicas (Búsqueda Binaria)")
#     print("7. Mostrar la lista base actual de canciones")
#     print("0. Salir")
#     print("="*60)


# def main():
#     # Cargar y mostrar la lista inicial
#     canciones = obtener_lista_canciones()
#     print("="*60)
#     print("                  BASE DE DATOS INICIAL")
#     print("="*60)
#     imprimir_tabla(f"Lista cargada inicialmente ({len(canciones)} canciones)", canciones)

#     while True:
#         mostrar_menu()
#         opcion = input("Seleccione una opción (0-7): ").strip()

#         if opcion == "1":
#             print("\n>>> ITEM A: SELECCIÓN DE CRITERIO DE ORDENAMIENTO <<<")
#             print("a. Ordenar por Nombre de Canción (Quicksort)")
#             print("b. Ordenar por Banda o Artista (Quicksort)")
#             print("c. Ordenar por Año de Lanzamiento (Counting Sort)")
            
#             sub_opcion = input("Elija el criterio de ordenamiento (a/b/c): ").strip().lower()
            
#             mapa_opciones = {"a": "1", "b": "2", "c": "3"}
#             criterio = mapa_opciones.get(sub_opcion)

#             if criterio:
#                 lista_ordenada, descripcion = ordenar_por_criterio(canciones, criterio)
#                 imprimir_tabla(f"Resultado del Ordenamiento por {descripcion}", lista_ordenada)
#             else:
#                 print("\n[ERROR] Criterio de ordenamiento no válido.")

#         elif opcion == "2":
#             print("\n>>> EJECUTANDO ITEM B: VERIFICAR ARTISTAS <<<")
#             for artista in ["Audioslave", "Rolling Stones"]:
#                 existe = existe_artista(canciones, artista)
#                 print(f"• ¿Existe alguna canción de {artista} en la lista?: {'Sí' if existe else 'No'}")

#         elif opcion == "3":
#             print("\n>>> EJECUTANDO ITEM C: MOSTRAR CANCIONES DE NIRVANA <<<")
#             canciones_nirvana = obtener_canciones_por_artista(canciones, "Nirvana")
#             imprimir_tabla("Canciones de Nirvana", canciones_nirvana)

#         elif opcion == "4":
#             print("\n>>> EJECUTANDO ITEM D: AGREGAR CANCIÓN Y REORDENAR <<<")
#             print("Agregando 'By the Way' de Red Hot Chili Peppers (2002)...")
            
#             canciones, lista_reordenada = agregar_y_reordenar(
#                 canciones, "By the Way", "Red Hot Chili Peppers", 2002
#             )
#             print("[SISTEMA] Canción agregada exitosamente a la lista base.")
#             imprimir_tabla("Lista Reordenada por Nombre de Canción tras agregar el tema", lista_reordenada)

#         elif opcion == "5":
#             print("\n>>> EJECUTANDO ITEM E: CONTAR CANCIONES DE RHCP <<<")
#             total = contar_canciones_por_artista(canciones, "Red Hot Chili Peppers")
#             print(f"• Cantidad total de canciones de Red Hot Chili Peppers: {total}")

#         elif opcion == "6":
#             print("\n>>> EJECUTANDO ITEM F: BÚSQUEDA BINARIA <<<")
#             print("[INFO] Ordenando previamente la lista por nombre de canción para habilitar búsqueda binaria...")
#             lista_para_binaria = quicksort_por_campo(canciones, "cancion")

#             canciones_a_buscar = ["Fake Tales of San Francisco", "Black Hole Sun"]
#             for cancion in canciones_a_buscar:
#                 resultado = busqueda_binaria_cancion(lista_para_binaria, cancion)
#                 if resultado:
#                     print(f"• ENCONTRADA -> Canción: '{resultado['cancion']}' | Banda: {resultado['artista']} | Año: {resultado['anio']}")
#                 else:
#                     print(f"• NOTA -> La canción '{cancion}' no fue encontrada.")

#         elif opcion == "7":
#             imprimir_tabla(f"Lista Base Actual ({len(canciones)} canciones)", canciones)

#         elif opcion == "0":
#             print("\n[SISTEMA] Saliendo del programa... ¡Hasta luego!\n")
#             break

#         else:
#             print("\n[ERROR] Opción no válida. Por favor, ingrese un número del 0 al 7.")


# if __name__ == "__main__":
#     main()
    