#Listar los superheores que comienzan con  Bl, G, My, y W.

def filtrar_prefijos(lista, prefijos, indice: int = 0) -> None:
    if indice >= len(lista):
        return
    prefijos_lower = tuple(p.lower() for p in prefijos)
    if lista[indice].name.lower().startswith(prefijos_lower):
        print(lista[indice])
    filtrar_prefijos(lista, prefijos, indice + 1)