# b. escribir una función que muestre todas las notificaciones de Twitter,
#  cuyo mensaje incluya la palabra ‘Python’,sin perder datos en la cola;


from contar_notificacion import buscar_notificaciones

def twit_py(gestor):
    resultados, cantidad = buscar_notificaciones(gestor, app="Twitter", palabra="Python")

    print("\n──────────────────────────────────────────────")
    print(f"  Twitter con 'Python' ({cantidad} encontradas)")
    print("──────────────────────────────────────────────")
    for n in resultados:
        print(f"  [{n['hora']}] {n['app']} → {n['mensaje']}")
    print("──────────────────────────────────────────────")

    return resultados, cantidad
