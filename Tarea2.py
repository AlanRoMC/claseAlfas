"""
EJERCICIO #2
Funcion que pida tres numeros y encuentre el mayor
"""
def calculador(num1, num2, num3):
    if (num1 > num2):
        if (num1 > num3):
            return(num1)
    if (num2 > num1):
        if (num2 > num3):
            return(num2)
    if (num3 > num2):
        if (num3 > num1):
            return(num3)

if(__name__=='__main__'):
    numero1 = float(input("Ingrese el primer número: "))
    numero2 = float(input("Ingrese el segundo número: "))
    numero3 = float(input("Ingrese el tercer número: "))
    print("El número mayor es: ", calculador(numero1, numero2, numero3))
