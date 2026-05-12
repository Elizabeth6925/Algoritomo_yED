#d. mostrar todos los personajes cuyos nombre empiezan con C, D y G.

from  pila_muc import apilar, desapilar, esta_vacia 

def nombres_con_CDG(pila):
   
    
    aux = []
    resultado = {"c": [], "d": [], "g": []}
 
    while not esta_vacia(pila):
        personaje = desapilar(pila)
        inicial = personaje["nombre"][0].lower()
        if inicial in resultado:
            resultado[inicial].append(personaje["nombre"])
        aux.append(personaje)
 

    while aux:
        apilar(pila, aux.pop())
 
    print(" Personajes que empiezan con C, D o G")
    for letra, nombres in resultado.items():
        if nombres:
            print(f"  [{letra.upper()}]")
            for nombre in nombres:
                print(f"    - {nombre}")
        else:
            print(f"  No se encontró ningún nombre con la letra {letra.upper()}.")
    print()
 