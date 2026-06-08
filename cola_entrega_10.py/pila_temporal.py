# c. utilizar una pila para almacenar temporáneamente las notificaciones producidas entre las
# 11:43 y las 15:57, y determinar cuántas son.

from collections import deque 

def notific_hora (cola_original, hora_inicial, hora_final):

    aux = deque()

    pila = []

    while cola_original:
     
     hora , app , mensaje= cola_original.popleft()

     if hora_inicial <= hora <= hora_final :

        pila.append((hora, app , mensaje ))

        aux.append((hora,app, mensaje))


    while aux :
       
       cola_original.append(aux.popleft())

    return pila , len(pila)

def mostrar_pila(pila, titulo = "pila"):
   
    print(f"\n{'='*55}")

    print(f"  {titulo}  ({len(pila)} notificaciones)")
    print(f"{'='*55}")

 
    if not pila:

        print("  (vacia)")

    else:
        
        for i in range(len(pila) - 1, -1, -1):

            hora, app, mensaje = pila[i]

            etiqueta = " <- TOPE" if i == len(pila) - 1 else ""

            print(f"  [{hora}]  {app:<12}  {mensaje}{etiqueta}")
 
    print(f"{'='*55}")