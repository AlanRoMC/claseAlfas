class AparatoElectronico:

    marcA = "Troya"
    energia = True

    def __init__(self):
        print("Aparato Electronico creado")

    def encendido(self):
        if(self.energia == True):
            print("Estoy encendido")
            self.marca = True
        else:
            print("No tengo energía")

    def mostrarM(self):
        if(self.marca == True):
            print("Mi marca es: Troya")
        else:
            print("No estoy encendido")

prueba = AparatoElectronico()
prueba.encendido()
prueba.mostrarM()
