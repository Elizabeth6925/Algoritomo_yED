
#Mostrar los personajes que en su biografia incluyan la palabra time-traveling o suit.

def filtrar_bio(lista, palabras, indice: int = 0) -> None:
    if indice >= len(lista):
        return
    bio = lista[indice].short_bio.lower()
    if any(palabra.lower() in bio for palabra in palabras):
        print(lista[indice])
    filtrar_bio(lista, palabras, indice + 1)