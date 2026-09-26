# b. determinar si en la lista existe alguna canción de Audioslave y Rolling Stone;
# c. mostrar todas las canciones de Nirvana;
# e. determinar cuantas canciones de los Red Hot Chili Peppers hay en la lista;

def existe_artista(lista, artista_buscado):
    """Item B: Determina si existe al menos una canción del artista."""
    buscado = artista_buscado.lower()
    for c in lista:
        if c["artista"].lower() == buscado:
            return True
    return False


def obtener_canciones_por_artista(lista, artista_buscado):
    """Item C: Retorna todas las canciones de un artista."""
    buscado = artista_buscado.lower()
    return [c for c in lista if c["artista"].lower() == buscado]


def contar_canciones_por_artista(lista, artista_buscado):
    """Item E: Cuenta la cantidad de canciones de un artista."""
    buscado = artista_buscado.lower()
    return sum(1 for c in lista if c["artista"].lower() == buscado)