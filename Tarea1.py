"""
EJERCICIO #1
Funcion que pida un monto en dinero, decimal o no, y que devuelva el monto mas el 16 de IVA
"""
def iva(monto):
    monto = (monto * .16) + monto
    return(monto)

if(__name__=='__main__'):
    monto = float(input("Ingrese el monto de dinero para calcular el IVA: "))
    print("El monto con más IVA es de: ", iva(monto))
