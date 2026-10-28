# 23. Implementar un algoritmo que permita generar un árbol con los datos de la siguiente tabla


from criaturasdata import CRIATURAS_DATA


class Nodo():
    def __init__(self, nombre, derrotado_por):
        self.nombre = nombre                  # Nombre de la criatura
        self.izq = None
        self.der = None
        self.derrotado_por = derrotado_por    # Quién la derrotó (puede ser None)
        self.descripcion = ""                 # Breve descripción de la criatura
        self.capturada = None                 # g. Nombre del héroe o dios que la capturó
        self.nota = ""                        # k. Nota aclaratoria (Aves del Estínfalo)
        self.altura = 0


class ArbolBinario():
    def __init__(self):
        self.raiz = None

    def altura(self, nodo):
        if nodo is None:
            return -1
        return nodo.altura

    def actualizar_altura(self, nodo):
        if nodo is not None:
            alt_izq = self.altura(nodo.izq)
            alt_der = self.altura(nodo.der)
            nodo.altura = max(alt_izq, alt_der) + 1

    def rotacion_simple(self, nodo, control):
        if control:
            aux = nodo.izq
            nodo.izq = aux.der
            aux.der = nodo
        else:
            aux = nodo.der
            nodo.der = aux.izq
            aux.izq = nodo

        self.actualizar_altura(nodo)
        self.actualizar_altura(aux)
        return aux

    def rotacion_doble(self, nodo, control):
        if control:
            nodo.izq = self.rotacion_simple(nodo.izq, False)
            return self.rotacion_simple(nodo, True)
        else:
            nodo.der = self.rotacion_simple(nodo.der, True)
            return self.rotacion_simple(nodo, False)

    def auto_balancear(self, nodo):
        if nodo is not None:
            if self.altura(nodo.izq) - self.altura(nodo.der) == 2:
                if self.altura(nodo.izq.izq) >= self.altura(nodo.izq.der):
                    nodo = self.rotacion_simple(nodo, True)
                else:
                    nodo = self.rotacion_doble(nodo, True)
            elif self.altura(nodo.der) - self.altura(nodo.izq) == 2:
                if self.altura(nodo.der.der) >= self.altura(nodo.der.izq):
                    nodo = self.rotacion_simple(nodo, False)
                else:
                    nodo = self.rotacion_doble(nodo, False)
        return nodo

    def insertar(self, nombre, derrotado_por=None):
        def __insertar(nodo, nombre, derrotado_por=None):
            if nodo is None:
                nodo = Nodo(nombre, derrotado_por)
            elif nombre < nodo.nombre:
                nodo.izq = __insertar(nodo.izq, nombre, derrotado_por)
            else:
                nodo.der = __insertar(nodo.der, nombre, derrotado_por)

            nodo = self.auto_balancear(nodo)
            self.actualizar_altura(nodo)
            return nodo

        self.raiz = __insertar(self.raiz, nombre, derrotado_por)

    # a. Recorrido inorden: criatura y quién la derrotó
    def recorrido_inorden(self, nodo):
        if nodo is not None:
            self.recorrido_inorden(nodo.izq)
            print(f"Criatura: {nodo.nombre}, Derrotado por: {nodo.derrotado_por or 'nadie'}")
            if nodo.descripcion:
                print(f"  Descripción: {nodo.descripcion}")
            print(f"  Capturada por: {nodo.capturada or 'nadie'}")
            self.recorrido_inorden(nodo.der)

    def buscar(self, nombre):
        def __buscar(nodo, nombre):
            if nodo is None:
                return None

            if nodo.nombre == nombre:
                return nodo

            if nombre < nodo.nombre:
                return __buscar(nodo.izq, nombre)
            else:
                return __buscar(nodo.der, nombre)

        return __buscar(self.raiz, nombre)

    # b. Cargar descripción de una criatura
    def agregar_descripcion(self, nombre, descripcion):
        nodo = self.buscar(nombre)

        if nodo is not None:
            nodo.descripcion = descripcion

    # c. Mostrar toda la información de una criatura
    def mostrar_informacion(self, nombre):
        nodo = self.buscar(nombre)

        if nodo is not None:
            print(f"Nombre: {nodo.nombre}")
            print(f"Derrotado por: {nodo.derrotado_por or 'nadie'}")
            print(f"Descripción: {nodo.descripcion or 'No tiene descripción'}")
            print(f"Capturada por: {nodo.capturada or 'nadie'}")
            if nodo.nota:                                 # k.
                print(f"Nota: {nodo.nota}")
        else:
            print("La criatura no existe.")

    # h. Asignar la captura de una criatura a un héroe o dios
    def asignar_captura(self, nombre, heroe):
        nodo = self.buscar(nombre)

        if nodo is not None:
            nodo.capturada = heroe
            return True
        return False

    # n. Mostrar criaturas capturadas por un héroe (también usado por h)
    def criaturas_capturadas_por(self, heroe):
        print(f"\nCriaturas capturadas por {heroe}:")
        encontradas = []

        def _rec(nodo):
            if nodo is not None:
                _rec(nodo.izq)
                if nodo.capturada == heroe:
                    encontradas.append(nodo.nombre)
                _rec(nodo.der)

        _rec(self.raiz)

        if not encontradas:
            print("   (ninguna)")
        for nombre in encontradas:
            print(f"   - {nombre}")

    # k. Agregar una nota aclaratoria a una criatura
    def agregar_nota(self, nombre, nota):
        nodo = self.buscar(nombre)
        if nodo is not None:
            nodo.nota = nota
            return True
        return False

    # j. Eliminar una criatura del árbol
    def eliminar_criatura(self, nombre):
        self.raiz = self._eliminar(self.raiz, nombre)

    def _eliminar(self, nodo, nombre):
        if nodo is None:
            return None

        if nombre < nodo.nombre:
            nodo.izq = self._eliminar(nodo.izq, nombre)
        elif nombre > nodo.nombre:
            nodo.der = self._eliminar(nodo.der, nombre)
        else:
            # Caso 1: hoja
            if nodo.izq is None and nodo.der is None:
                return None
            # Caso 2: un solo hijo
            elif nodo.izq is None:
                return nodo.der
            elif nodo.der is None:
                return nodo.izq
            # Caso 3: dos hijos -> sucesor inorden
            else:
                sucesor = self._minimo(nodo.der)
                nodo.nombre = sucesor.nombre
                nodo.derrotado_por = sucesor.derrotado_por
                nodo.descripcion = sucesor.descripcion
                nodo.capturada = sucesor.capturada
                nodo.nota = sucesor.nota
                nodo.der = self._eliminar(nodo.der, sucesor.nombre)

        nodo = self.auto_balancear(nodo)
        self.actualizar_altura(nodo)
        return nodo

    def _minimo(self, nodo):
        while nodo.izq is not None:
            nodo = nodo.izq
        return nodo

    # l. Renombrar una criatura (elimina e inserta para mantener el orden del AVL)
    def renombrar(self, nombre_viejo, nombre_nuevo):
        nodo = self.buscar(nombre_viejo)
        if nodo is None:
            return False
        derrotado_por = nodo.derrotado_por
        descripcion = nodo.descripcion
        capturada = nodo.capturada
        nota = nodo.nota
        self.eliminar_criatura(nombre_viejo)
        self.insertar(nombre_nuevo, derrotado_por)
        nuevo = self.buscar(nombre_nuevo)
        nuevo.descripcion = descripcion
        nuevo.capturada = capturada
        nuevo.nota = nota
        return True

    # m. Listado por nivel (BFS)
    def listado_por_nivel(self):
        if self.raiz is None:
            print("(árbol vacío)")
            return
        from collections import deque
        cola = deque([(self.raiz, 0)])
        nivel_actual = -1
        while cola:
            nodo, nivel = cola.popleft()
            if nivel != nivel_actual:
                nivel_actual = nivel
                print(f"\nNivel {nivel}:")
            print(f"  - {nodo.nombre} (derrotada por: {nodo.derrotado_por or 'nadie'})")
            if nodo.izq:
                cola.append((nodo.izq, nivel + 1))
            if nodo.der:
                cola.append((nodo.der, nivel + 1))


# i. Búsqueda por coincidencia (función suelta, se mantiene como ya funcionaba)
def busqueda_coincidencia(nodo, subcadena):
    resultados = []

    def __busqueda_coincidencia(nodo, subcadena):
        if nodo is not None:
            __busqueda_coincidencia(nodo.izq, subcadena)
            if subcadena.lower() in nodo.nombre.lower():
                resultados.append(nodo)
            __busqueda_coincidencia(nodo.der, subcadena)

    __busqueda_coincidencia(nodo, subcadena)
    return resultados