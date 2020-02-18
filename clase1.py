'''
# Entrada de datos
nombre = input("Ingresa tú nombre: ")
edad = int(input("Ingresa tú edad: "))
print("Hola ", nombre, " tu edad es: ", edad)
print("Tú edad en 10 años será: ", (edad+10))'''

'''
# Variables globales y locales
x = "global"

def miFuncion():
    x = "local"
    global x
    x = "CD"
    print("Hola soy una Variable", x)

miFuncion()
print("Hola soy una Variable", x)

# Estructura de dato (for, while)
año = 2000
while(año < 2020):
    print("Año: ", str(año))
    año += 1

for variable in range(0,10):
    print(variable)

string = "Hola Mundo"
for letra in string:
    print(letra)
'''

'''
listas = [[1,2,3],[4,5,6],[7,8,9]]

string = ""
for lista in listas:
    #print(lista)

    for numero in lista:
        #print(numero)
        string += str(numero) + " "
print(string)
'''
