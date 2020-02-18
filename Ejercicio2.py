"""
EJERCICIO #2
Crea un programa que pida un numero entero positivo y le haga saber al usuario si es par o primo
"""
if(__name__=='__main__'):
    numero = int(input("Ingresa un número: "))
    if ((numero % 2) == 0):
        print("Es par")
    else:
        print("Es impar")
