"""
EJERCICIO #4
Funcion que calcule el factorial de un numero
"""
def factorial(valor, acomulador):
  contador = valor
  for i in range (0, contador):
    acomulador = (acomulador * valor)
    valor = int(valor - 1)
  return(acomulador)

if(__name__=='__main__'):
  numeros  = int(input("De cuántos números desea calcular su factorial: "))
  contador = int(0)
  acomulador = int(1)
  for i in range (0, numeros):
      numero = int(input("Ingrese un número: "))
      print("El factorial de: ", numero, " es: ", factorial(numero, acomulador))
