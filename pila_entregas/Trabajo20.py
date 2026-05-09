#Realizar un algoritmo que registre los movimientos de un robot, los datos que se guardan son
#cantidad de pasos y dirección –suponga que el robot solo puede moverse en ocho direcciones:
#norte, sur, este, oeste, noreste, noroeste, sureste y suroeste–. Luego desarrolle otro algoritmo
#que genere la secuencia de movimientos necesarios para hacer volver al robot a su lugar de
#partida, retornando por el mismo camino que fue.

import movimiento

print("Registro de movimientos del robot")
print("Escriba 'fin' para terminar")

while True:

    pasos = input("Ingrese cantidad de pasos: ")

    if pasos.lower() == "fin":
        break

    direccion = input(
        "Ingrese dirección (norte, sur, este, oeste, noreste, noroeste, sureste, suroeste): "
    )

    movimiento.registrar_movimiento(int(pasos), direccion)

movimientos_retorno = movimiento.generar_movimientos_retorno()

print("\nMovimientos de retorno:")

for pasos, direccion in movimientos_retorno:
    print(f"{pasos} pasos hacia {direccion}")
    