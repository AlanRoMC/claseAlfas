"""
EJERCICIO #3
Funcion que pida N numeros y los multiplique todos
"""
def multiplicador(numeros):
    multiplicador = float(1)
    for i in range(0, numeros):
        numero = float(input("Ingrese el número: "))
        multiplicador *= numero
    return(multiplicador)

if(__name__=='__main__'):
    numeros = int(input("¿Cuántos números desea multiplicar? "))
    print("El resultado de la operación es de: ", multiplicador(numeros))
