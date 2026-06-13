# b. mostrar los nombre de los superhéroes femeninos;
# c. mostrar los nombres de los personajes masculinos;

from crear_cola import crear_cola, desencolar, encolar, esta_vacia

def filtrar_por_genero(cola, genero):

    resultado = crear_cola()
    aux = crear_cola()
    
    while not esta_vacia(cola):

        p = desencolar(cola)

        if p["genero"] == genero:

            encolar(resultado, p)

        encolar(aux, p)
    
    while not esta_vacia(aux):
        
        encolar(cola, desencolar(aux))
    
    return resultado

