# c. mostrar los nombres de los personajes masculinos;

from crear_cola_mcu import mostrar_cola

def separar_por_genero(cola):

    femeninos = crear_cola_m()
    masculinos = crear_cola_f()
    
    for p in cola:
        if p["genero"] == "F":
            encolar(femeninos, p)
        else:
            encolar(masculinos, p)
    
    return femeninos, masculinos