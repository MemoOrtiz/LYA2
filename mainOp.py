#Hecho por Adrian, Martin y Guillermo
from Arbol_Expresiones import Arbol_Expresiones


def main():
    arbol = Arbol_Expresiones()

    expresion = "((4+3+4)*2^5*4)+(3+4*6-2)"

    arbol.crea_ABE(expresion)


    print("Contenido del arbol en preorden: ")
    print(arbol.imprimir(0))
    #print("El resultado es: " , arbol.evalua())
    print("\n--------------------------------------------------")
    
    print("\nContenido del arbol en inorden: ")
    print(arbol.imprimir(2))
    #print("El resultado es: " , arbol.evalua())
    print("\n--------------------------------------------------")
    print("\nContenido del arbol en postorden: ")
    print(arbol.imprimir(1))
    #print("El resultado es: " , arbol.evalua())
    
    # Generar triplos
    triplos = arbol.genera_triplos()
    print("\nTriplos generados:")
    for triplo in triplos:
        print(triplo)
    
    # Generar  cuádruplos
    cuadruplos = arbol.genera_cuadruplos()
    print("\nCuádruplos generados:")
    for cuadruplo in cuadruplos:
        print(cuadruplo)
    

if __name__ == "__main__":
    main()
