#Realizar un algoritmo que registre los movimientos de un robot, los datos que se guardan son
#cantidad de pasos y dirección –suponga que el robot solo puede moverse en ocho direcciones:
#norte, sur, este, oeste, noreste, noroeste, sureste y suroeste–. Luego desarrolle otro algoritmo
#que genere la secuencia de movimientos necesarios para hacer volver al robot a su lugar de
#partida, retornando por el mismo camino que fue.
 
import movimiento 
from reversa import obtener_direccion_opuesta   
print("Registro de movimientos del robot con numero y direccion (norte,sur,este,oeste,noreste,noroeste,sureste,suroeste):")

# Ejemplo de uso
movimiento.registrar_movimiento(5, 'norte')    
movimiento.registrar_movimiento(3, 'este')
movimiento.registrar_movimiento(2, 'suroeste')
movimientos_retorno = movimiento.generar_movimientos_retorno()
print("Movimientos de retorno:")

for pasos, direccion in movimientos_retorno:
    print(f"{pasos} pasos hacia {direccion}")




