'''
#Ejercicio 1

numero = int(input("Ingresa un número: "))
numero2 = int(input("Ingresa otro número: "))

try:
    print(numero/numero2)
except ArithmeticError as err:
    print("La operación no pudo ser realizada.")
    print("Error: " + str(err))
'''

'''
#Ejercicio 2
#Escribe una funcion que sume 10 y lo multiplique por 2 a un numero pedido a consola

numero = int(input("Ingresa un número: "))
numero2 = int(input("Ingresa otro número: "))
numero3 = int(input("Ingresa otro número: "))
resultado = lambda numero, numero2, numero3: numero + numero2 + numero3
print(resultado(numero, numero2, numero3))
'''

'''
resultado = lambda x, y, z: (z*z) + x + y
print(resultado(numero, numero2, numero3))
'''

'''
#Ejercicio 2 - MAP
#Estructura de la funcion MAP:
map(funcion_a_realizar, estructura_de_dato)

#Luego, mediante map, pasale la siguiente lista como parametro, imprimiendo
numeros = [2,3,4,5]

numeros = [2,3,4,5]
def cuadrado(numero):
    return numero * numero
print(list(map(cuadrado, numeros)))
'''

'''
#Ejercicio 3 MAP y LAMBDA
#Resuelve el ejercicio anterior utilizando MAP y LAMBDA

numeros = [2,3,4,5]
resultado = list(map(lambda n: n*n, numeros))
print(resultado)
'''

'''
#ESTRUCTURA DE UNA FUNCION EN PYTHON
def nombre_de_la_funcion(argumentos):
    operacion
    operacion2
    print(operacion3)
    return nombre_variable
'''
'''
def saludo(nombre):
    return "Hola " + nombre + "!!"

nombre = input("Ingresa tú nombre: ")
print(saludo(nombre))
'''
'''
def suma(numero1, numero2):
    #return numero1 + numero2

def resta(numero1, numero2):
    return numero1 - numero2

numero = int(input("Ingresa un numero: "))
numero2 = int(input("Ingresa un numero: "))
print(resta(numero, numero2))
'''
'''
def posicional(*argumentos):
    for arg in argumentos:
        print(arg)
    return None

posicional(1, "Argumento posicional #2", [1,2,3,4,5], "Args #4")
'''
'''
def nombre(**kwargs):
    for argumento in kwargs:
        for valor in argumento:
            print(str(argumento) + " = " + str(kwargs[argumento]))

    return None
nombre(a = 1, b = "Hola", c = "Adios", d = 4.2)
'''

'''
#Pasar varios argumentos con o sin nombre
#Para los argumentos sin nombre, debera imprimir su valor
#Para los argumentos con nombre, debera imprimir el nombre y su valor

def combinaciones(*args, **kwargs):
    suma = 0
    for arg in args:
        suma += arg
    print("Suma= " + str(suma))

    for kwarg in kwargs:
        print(str(kwarg) + " = " + str(kwargs[kwarg]))
    return None

combinaciones(2, 4, 6, a = "A", b = "B", c = "C")
'''
