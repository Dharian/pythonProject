class Cuadrado:
    def __init__(self):
        self.lado = int(input("Cuanto mide un lado? "))

    def calcularSuperficie(self):
        resultado=self.lado+self.lado
        print(" El valor total de la superficie es: ", resultado)

    def calcularArea(self):
        resultado=self.lado*self.lado
        print(" El valor total del area es: ", resultado)


Cuadrado1=Cuadrado()
Cuadrado1.calcularSuperficie()
Cuadrado1.calcularArea()


Cuadrado2= Cuadrado()    
Cuadrado2.calcularSuperficie()
Cuadrado2.calcularArea()
