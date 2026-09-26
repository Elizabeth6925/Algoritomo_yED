#Se cuenta con una lista de canciones, de cada una de estas conocemos su nombre,
#  nombre de la bandas o artista, y el año de lanzamiento del álbum;
# desarrollar las funciones necesarias para dar solución a las siguientes tareas:
#CREADOR DE LA LISTA DE CANCIONES

# def crear_lista_canciones():
#     lista_canciones = []
#     while True:
#         nombre_cancion = input("Ingrese el nombre de la canción (o 'salir' para terminar): ")
#         if nombre_cancion.lower() == 'salir':
#             break
#         banda_artista = input("Ingrese el nombre de la banda o artista: ")
#         anio_lanzamiento = input("Ingrese el año de lanzamiento del álbum: ")
#         cancion = {
#             'nombre': nombre_cancion,
#             'banda_artista': banda_artista,
#             'anio': anio_lanzamiento
#         }
#         lista_canciones.append(cancion)
#     return lista_canciones


def obtener_lista_canciones():
    """Retorna la lista inicial de canciones predeterminada con los nuevos artistas."""
    return [
        # Canciones originales
        {"cancion": "Fake Tales of San Francisco", "artista": "Arctic Monkeys", "anio": 2006},
        {"cancion": "Black Hole Sun", "artista": "Soundgarden", "anio": 1994},
        {"cancion": "Smells Like Teen Spirit", "artista": "Nirvana", "anio": 1991},
        {"cancion": "Californication", "artista": "Red Hot Chili Peppers", "anio": 1999},
        {"cancion": "Like a Stone", "artista": "Audioslave", "anio": 2002},
        {"cancion": "Paint It Black", "artista": "Rolling Stones", "anio": 1966},
        {"cancion": "Come As You Are", "artista": "Nirvana", "anio": 1991},
        {"cancion": "Otherside", "artista": "Red Hot Chili Peppers", "anio": 1999},
        {"cancion": "Billie Jean", "artista": "Michael Jackson", "anio": 1982},
        {"cancion": "Beat It", "artista": "Michael Jackson", "anio": 1982},
        {"cancion": "Smooth Criminal", "artista": "Michael Jackson", "anio": 1987},
        {"cancion": "Yendo a la casa de Damian", "artista": "El Cuarteto de Nos", "anio": 2006},
        {"cancion": "Lo malo de ser bueno", "artista": "El Cuarteto de Nos", "anio": 2012},
        {"cancion": "Enamorado tuyo", "artista": "El Cuarteto de Nos", "anio": 2012},
        {"cancion": "El Viejo", "artista": "La Vela Puerca", "anio": 2001},
        {"cancion": "Zafar", "artista": "La Vela Puerca", "anio": 2004},
        {"cancion": "Llenos de magia", "artista": "La Vela Puerca", "anio": 2004}
    ]

def agregar_cancion(lista, cancion, artista, anio):
    """Item D: Agrega una nueva canción a la lista existente."""
    nueva = {"cancion": cancion, "artista": artista, "anio": int(anio)}
    lista.append(nueva)
    return lista