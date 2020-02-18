'''
Comandos:
1 encender()
2 despegar()
3 volar()
4 detenrse()
5 aterrizar()
5.1 cargarGas()
5.2 mostrarGas()
6 apagar()
'''

class Dron:

    color = "Negro"
    helices = True
    bateria = int(5)
    gasolina = int(10)
    marca = "Troya"

    def __init__(self):
        print("Dron creado")

    def encender(self):
        if (self.helices == True and (self.gasolina > 0 or self.bateria > 0)):
            print("Estoy encendido")
            self.despegue = True
            self.gasolina -= 1
            self.bateria -= 1
            self.mGas = True
            self.apagar = True
        else:
            print("No tengo helices, gasolina y/o bateria para DESPEGAR")

    def despegar(self):
        if (self.despegue == True):
            print("Estoy despegando")
            self.movimiento = True
        else:
            print("Me encuentro indispuesto a realizar la accion de DESPEGAR")

    def volar(self):
        if (self.movimiento == True):
            print("Estoy volando")
            self.detenerse = True
        else:
            print("Me encuentro indispuesto a realizar la accion de VOLAR")

    def detenerte(self):
        if (self.detenerse == True):
            print("Me detuve")
            self.movimiento = True
            self.descender = True
        else:
            print("Me encuentro indispuesto a DETENERME")

    def aterrizar(self):
        if (self.descender == True):
            print("Estoy aterrizando")
            self.mGas = True
            self.despegue = True
            self.apagar = True
        else:
            print("Me encuentro indispuesto a ATERRIZAR")

    def mostrarGas(self):
        if (self.mGas == True):
            gasolina = int(10-1)
            bateria = int(5-1)
            print("Cuento con: ",gasolina,"/10 de gasolina y con bateria: ",bateria,"/5")
            self.cGas = True
            self.apagar = True
            self.despegue = True
        else:
            print("Me encuentro indispuesto a mostrate mi nivel de gasolina en este momento")

    def cargarGas(self):
        if (self.cGas == True):
            print("Ya cargaste gas")
            self.despegue = True
            self.apagar = True
        else:
            print("Me encuentro indispuesto a cargar gasolina en este momento")

    def apagarse(self):
        if (self.apagar == True):
            print("Me apagare")
        else:
            print("Me encuentro indispuesto a APAGARME en este momento")


prueba = Dron()
prueba.encender()
prueba.despegar()
prueba.volar()
prueba.detenerte()
prueba.aterrizar()
prueba.mostrarGas()
prueba.cargarGas()
prueba.apagarse()
