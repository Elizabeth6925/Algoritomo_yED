# 23. Implementar un algoritmo que permita generar un árbol con los datos de la siguiente tabla


from criaturasdata import CRIATURAS_DATA


class Nodo():
    def __init__(self, nombre, derrotado_por):
        self.nombre = nombre                  # Nombre de la criatura
        self.izq = None
        self.der = None
        self.derrotado_por = derrotado_por    # Quién la derrotó (puede ser None)
        self.descripcion = ""   # Breve descripción de la criatura
        self.capturada = None  # Nombre del héroe o dios que la capturó punto g 
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

    def recorrido_inorden(self, nodo):
        if nodo is not None:
            self.recorrido_inorden(nodo.izq)
            print(f"Criatura: {nodo.nombre}, Derrotado por: {nodo.derrotado_por}")
            if nodo.descripcion:
                print(f"  Descripción: {nodo.descripcion}")
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

    def agregar_descripcion(self, nombre, descripcion):
        nodo = self.buscar(nombre)

        if nodo is not None:
            nodo.descripcion = descripcion

    def mostrar_informacion(self, nombre):
        nodo = self.buscar(nombre)

        if nodo is not None:
            print(f"Nombre: {nodo.nombre}")
            print(f"Derrotado por: {nodo.derrotado_por}")
            print(f"Descripción: {nodo.descripcion}")
        else:
            print("La criatura no existe.")

    def recorrido_inorden(self, nodo):
        if nodo is not None:
            self.recorrido_inorden(nodo.izq)
            print(f"Criatura: {nodo.nombre}, Derrotado por: {nodo.derrotado_por}")
            if nodo.descripcion:
                print(f"  Descripción: {nodo.descripcion}")
            self.recorrido_inorden(nodo.der)




