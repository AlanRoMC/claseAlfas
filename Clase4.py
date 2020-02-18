class Automovil:

    color = "Rojo"
    motor = True
    llantas = 4
    gasolina = 10
    asientos = 5
    marca = "Nissan"
    movimiento = False

    def __init__(self):
        print("Automovil creado")

    def avanzar(self):
        if (self.llantas == False and self.gasolina > 0 and self.motor == True):
            print("Estoy avanzando")
            self.movimiento = True
            self.gasolina -= 1
        else:
            print("No tengo llantas o gasolina o motor para avanzar o me estoy moviendo")

    def detenerse(self):
        if(self.movimiento == True):
            self.movimiento = False
            print("Me detengo")
        else:
            print("No me estoy moviendo")


    def retroceder(self):
        if(self.movimiento == False and self.gasolina > 0 and self.motor):
            print("Estoy retrocediendo")
        else:
            print("No tengo llantas o gasolina o motor para retroceder")



bocho = Automovil()
tsuru = Automovil()

print("Soy Bocho")
bocho.detenerse()
bocho.avanzar()
bocho.detenerse()
bocho.retroceder()
