"""
EJERCICIO #4
Crea un programa que le pida al usuario una palabra y muestre si esa palabra es un palindromo
NOTA: un palindromo es una palabra que se puede escribir al derecho y al reves de la misma manera.
(Por ejemplo: ana, ala, oso)
"""
if(__name__=='__main__'):
    palabra = str(input("Ingrese una palabra: "))
    if (palabra == palabra[::-1]):
        print("La palabra es Palindroma")
    else:
        print("La palabra no es Palindroma")
