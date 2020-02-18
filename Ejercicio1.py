'''
EJERCICIO #1
Crea un programa que pida el nombre y la edad del usuario.
El programa debera imprimir en que año el usuario cumplira 100 años
'''
if(__name__=='__main__'):
    nombre = str(input("Ingresa tú nombre: "))
    edad = int(input("Ingresa tú edad: "))
    cumple = int((100-edad)+2020)
    print("Hola ", nombre, " cumpliras 100 años en el año:", cumple)
