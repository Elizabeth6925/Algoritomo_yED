

from pila_entregas.reversa import obtener_direccion_opuesta


registro_movimientos = [] 

def registrar_movimiento(pasos, direccion):
    registro_movimientos.append((pasos, direccion)) 
def generar_movimientos_retorno():
    movimientos_retorno = []
    for pasos, direccion in reversed(registro_movimientos):
        direccion_retorno = obtener_direccion_opuesta(direccion)
        movimientos_retorno.append((pasos, direccion_retorno))
    return movimientos_retorno 
