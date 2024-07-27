
from Pila import Pila


class nodoArbolExpresiones(object):
    dato = None
    izquierdo = None
    derecho = None


class Arbol_Expresiones(object):

    def __init__(self):
        self.raiz = None

    def arbol_vacio(self):
        return self.raiz == None

    def reinicializar(self):
        self.raiz = None

    def imprimir(self, tipo):
        cadena = ""
        if tipo == 0:
            cadena = self.__prefijo(self.raiz)
        elif tipo == 1:
            cadena = self.__postfijo(self.raiz)
        elif tipo == 2:
            cadena = self.__infijo(self.raiz)

        return cadena

    def __prefijo(self, subarbol):
        cadena = ""
        if subarbol !=  None:
            cadena += subarbol.dato + "\n" + self.__prefijo(subarbol.izquierdo) + self.__prefijo(subarbol.derecho)
        return cadena

    def __postfijo(self, subarbol):
        cadena = ""
        if subarbol != None:
            cadena += self.__postfijo(subarbol.izquierdo) + self.__postfijo(subarbol.derecho) + subarbol.dato + "\n"
        return cadena

    def __infijo(self, subarbol):
        cadena = ""
        if subarbol != None:
            cadena += self.__infijo(subarbol.izquierdo) + subarbol.dato + "\n" + self.__infijo(subarbol.derecho) 
        return cadena

    def __crea_sub_arbol(self, operando2, operando1, operador):

        operador.izquierdo = operando1
        operador.derecho = operando2
        return operador

    def __prioridad(self, caracter):
        if caracter in ["^"]:
            prioridad = 3

        elif caracter in ["*", "/"]:
            prioridad = 2

        elif caracter in ["+", "-"]:
            prioridad = 1
        else:
            prioridad = 0

        return prioridad

    def __es_operador(self, caracter):
        return caracter in ["(", ")", "^", "*", "/", "+", "-"]

    def crea_ABE(self, cadena):
        pila_operandos = Pila()
        pila_operadores = Pila()

        for caracter in cadena:
            token = nodoArbolExpresiones()
            token.dato = caracter

            if not self.__es_operador(caracter):
                pila_operandos.insertar(token)

            else:
                if caracter in ["("]:
                    pila_operadores.insertar(token)
                elif caracter in [")"]:
                    tope = pila_operadores.tope_pila()
                    while not pila_operadores.pila_vacia() and tope.dato not in ["("]:
                        operando2 = pila_operandos.quitar()
                        operando1 = pila_operandos.quitar()
                        operador = pila_operadores.quitar()
                        nuevo_operando = self.__crea_sub_arbol(operando2, operando1, operador)
                        pila_operandos.insertar(nuevo_operando)
                        tope = pila_operadores.tope_pila()
                    operador = pila_operadores.quitar()
                else:
                    tope = pila_operadores.tope_pila()
                    while not pila_operadores.pila_vacia() and \
                            self.__prioridad(caracter) <= self.__prioridad(tope.dato):
                        operando2 = pila_operandos.quitar()
                        operando1 = pila_operandos.quitar()
                        operador = pila_operadores.quitar()
                        nuevo_operando = self.__crea_sub_arbol(operando2, operando1, operador)
                        pila_operandos.insertar(nuevo_operando)
                        tope = pila_operadores.tope_pila()
                    pila_operadores.insertar(token)

        while not pila_operadores.pila_vacia():
            operando2 = pila_operandos.quitar()
            operando1 = pila_operandos.quitar()
            operador = pila_operadores.quitar()
            nuevo_operando = self.__crea_sub_arbol(operando2, operando1, operador)
            pila_operandos.insertar(nuevo_operando)

        self.raiz = pila_operandos.quitar()

    def evalua(self):
        return self.__evalua_expresion(self.raiz)

    def __evalua_expresion(self, subarbol):

        acum = 0.0
        if not self.__es_operador(subarbol.dato):
            return float(subarbol.dato)
        else:
            if subarbol.dato in ["^"]:
                acum += self.__evalua_expresion(subarbol.izquierdo) ** self.__evalua_expresion(subarbol.derecho)
            elif subarbol.dato in ["*"]:
                acum += self.__evalua_expresion(subarbol.izquierdo) * self.__evalua_expresion(subarbol.derecho)
            elif subarbol.dato in ["/"]:
                acum += self.__evalua_expresion(subarbol.izquierdo) / self.__evalua_expresion(subarbol.derecho)
            elif subarbol.dato in ["+"]:
                acum += self.__evalua_expresion(subarbol.izquierdo) + self.__evalua_expresion(subarbol.derecho)
            elif subarbol.dato in ["-"]:
                acum += self.__evalua_expresion(subarbol.izquierdo) - self.__evalua_expresion(subarbol.derecho)
        return acum

    def genera_triplos(self):
        self.triplos = []
        self.__genera_triplos(self.raiz)
        return self.triplos
    
    def __genera_triplos(self, subarbol):
        if subarbol:
            if self.__es_operador(subarbol.dato):
                izquierda = self.__genera_triplos(subarbol.izquierdo)
                derecha = self.__genera_triplos(subarbol.derecho)
                triplo = (subarbol.dato, izquierda, derecha)
                self.triplos.append(triplo)
                return f"T{len(self.triplos)}"
            else:
                return subarbol.dato
    
    def genera_cuadruplos(self):
        self.cuadruplos = []
        self.__genera_cuadruplos(self.raiz)
        return self.cuadruplos

    def __genera_cuadruplos(self, subarbol):
        if subarbol:
            if self.__es_operador(subarbol.dato):
                izquierda = self.__genera_cuadruplos(subarbol.izquierdo)
                derecha = self.__genera_cuadruplos(subarbol.derecho)
                temp = f"T{len(self.cuadruplos) + 1}"
                cuadruplo = (subarbol.dato, izquierda, derecha, temp)
                self.cuadruplos.append(cuadruplo)
                return temp
            else:
                return subarbol.dato
#lo de triplos y cuadruplos
    def ejecuta_triplos(self):
        resultados = {}
        for operador, arg1, arg2 in self.triplos:
            if operador == '*':
                # Verifica si arg1 es un identificador temporal y obtiene su valor
                valor1 = resultados[arg1] if arg1.startswith('T') else float(arg1)
                # Verifica si arg2 es un identificador temporal y obtiene su valor
                valor2 = resultados[arg2] if arg2.startswith('T') else float(arg2)
                # Calcula el resultado y lo almacena con un nuevo identificador temporal
                resultados[f"T{len(resultados)+1}"] = valor1 * valor2
            # Agrega condiciones para otros operadores si es necesario
        return resultados

    def ejecuta_cuadruplos(self):
        resultados = {}
        for cuadruplo in self.cuadruplos:
            op, arg1, arg2, res = cuadruplo
            # Obtener el valor de arg1
            if arg1.startswith('T'):
                valor1 = resultados[arg1]
            else:
                valor1 = float(arg1)
            # Obtener el valor de arg2
            if arg2.startswith('T'):
                valor2 = resultados[arg2]
            else:
                valor2 = float(arg2)
            
            # Realizar la operación
            if op == '+':
                resultados[res] = valor1 + valor2
            elif op == '-':
                resultados[res] = valor1 - valor2
            elif op == '*':
                resultados[res] = valor1 * valor2
            elif op == '/':
                resultados[res] = valor1 / valor2
        return resultados