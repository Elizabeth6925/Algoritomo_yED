

def obtener_direccion_opuesta(direccion):
    direcciones_opuestas = {
        'norte': 'sur',
        'sur': 'norte',
        'este': 'oeste',
        'oeste': 'este',
        'noreste': 'suroeste',
        'noroeste': 'sureste',
        'sureste': 'noroeste',
        'suroeste': 'noreste'
    }

    return direcciones_opuestas.get(direccion, None)            

