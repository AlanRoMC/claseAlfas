"""
EJERCICIO #5
Pide un string y debera imprimirse en orden reverso
ejemplo: "Uriel se encuentra ocupado"
Salida: "ocupado encuentra se Uriel"
"""
def reverso(texto):
    textoInvertido = Text.split('  ')
    textoInver = ""
    for i in textoInvertido[::-1]:
        textoInver += i + " "
    return(textoInver)

if(__name__=='__main__'):
    texto = str(input("Ingrese un texto: "))
    print(reverso(texto))
