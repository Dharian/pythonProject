class Operaciones:

    def __init__(self):
        self.num1=int(input("Primer valor: "))
        self.num2=int(input("Segundo valor: "))
        self.sumar()
        self.restar()
        self.multiplicar()
        self.division()

    def sumar(self):
        resultado=self.num1+self.num2
        print(resultado)

    def restar(self):
        resultado=self.num1-self.num2
        print(resultado)

    def multiplicar(self):
        resultado=self.num1*self.num2
        print(resultado)

    def division(self):
        resultado=self.num1/self.num2
        print(resultado)

Operacion1=Operaciones()
Operacion2=Operaciones()
