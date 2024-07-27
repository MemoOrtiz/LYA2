#Hecho por Adrian, Martin y Guillermo
from Arbol_Expresiones import Arbol_Expresiones


def imprimir_recorrido(arbol, orden, nombre_orden):
    print(f"\nContenido del árbol en recorrido {nombre_orden}: ")
    print(arbol.imprimir(orden))
    print("\n" + "-"*50)


def imprimir_estructuras(estructuras, nombre):
    """Imprime los triplos o cuádruplos generados."""
    print(f"\n{nombre} generados:")
    for estructura in estructuras:
        print(estructura)

def main():
    arbol = Arbol_Expresiones()

    expresion = "11*32*4+(3+4*6-2)"

    arbol.crea_ABE(expresion)

    imprimir_recorrido(arbol, 0, "preorden")
    imprimir_recorrido(arbol, 2, "inorden")
    imprimir_recorrido(arbol, 1, "postorden")
    
    # Generar e imprimir triplos y cuádruplos
    triplos = arbol.genera_triplos()
    imprimir_estructuras(triplos, "Triplos")

    cuadruplos = arbol.genera_cuadruplos()
    imprimir_estructuras(cuadruplos, "Cuádruplos")
    

    
    


if __name__ == "__main__":
    main()
