"""
EJERCICIO #5
Crea un programa con un diccionario que contenga de llave un nombre
y de valor el cumpleaños de esta persona.
El programa pedira el nombre de la persona y se debera imprimir la fecha de su cumpleaños
"""
if(__name__=='__main__'):
    diccionario = {'Alan':'16/05/2001','Armando':'30/08/2000','Israel':'15/07/2000'}
    nombre = input("Ingresa el nombre: ")
    print(diccionario[nombre])
    diccionario['Fernando'] = '29/03/2000'
    nombre = input("Ingresa el nombre: ")
    print(diccionario[nombre])
