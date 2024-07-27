#Hecho por Guillermo Ortiz Aguilar
class nodopila(object):
    dato = None
    siguiente = None


class Pila(object):

    def __init__(self):
        self.tope = None

    def reiniciar(self):
        self.tope = None

    def insertar(self, dato):
        nodo = nodopila()
        nodo.dato = dato
        nodo.siguiente = self.tope
        self.tope = nodo

    def quitar(self):
        x = self.tope.dato
        nodo_eliminar = self.tope
        self.tope = self.tope.siguiente
        nodo_eliminar.siguiente = None
        return x

    def pila_vacia(self):
        return self.tope is None

    def tope_pila(self):
        if self.tope is not None:
            return self.tope.dato
        else:
            return None

    def imprimir(self):
        pil = Pila()
        cadena = ""
        while not self.pila_vacia():
            dato = self.quitar()
            cadena += str(dato) + "\n"
            pil.insertar(dato)

        while not pil.pila_vacia():
            dato = pil.quitar()
            self.insertar(dato)

        return cadena
