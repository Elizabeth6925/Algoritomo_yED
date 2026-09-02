from random import choice, randint 


tabla_legiones = [None] * 15


legiones = ["FL", "TF", "TK", "CT", "FN", "FO"]

print("Tabla de Legiones:") 
def hash_legion(clave) -> int:

    h=0
    for caracter in clave:

        h =h*33+ ord(caracter)

    return h % 15


for legion in legiones:

    print(legion )
    indice = hash_legion(legion)
 
    while tabla_legiones[indice] is not None:

        indice = (indice + 1) % len(tabla_legiones)
        
    tabla_legiones[indice] = legion 