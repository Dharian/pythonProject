class Socio:
    def  __init__(self):    
        self.nombre=str(input("Cual es tu nombre? "))
        self.antiguedad=int(input("Cuan antiguo es? "))
    
    


class Club:
    def __init__(self):
        self.socio1=Socio()
        self.socio2=Socio()
        self.socio3=Socio()
        self.MaxAntiguedad()

    def MaxAntiguedad(self):
        if self.socio1.antiguedad > self.socio2.antiguedad and self.socio1.antiguedad > self.socio3.antiguedad:
            print("El mas antiguo es ",self.socio1.nombre," con una antiguedad de: ",self.socio1.antiguedad)
        elif self.socio2.antiguedad > self.socio1.antiguedad and self.socio2.antiguedad > self.socio3.antiguedad:
            print("El mas antiguo es ",self.socio2.nombre," con una antiguedad de: ",self.socio2.antiguedad)
        elif self.socio3.antiguedad > self.socio2.antiguedad and  self.socio3.antiguedad >self.socio1.antiguedad:
           print("El mas antiguo es ",self.socio3.nombre," con una antiguedad de: ",self.socio3.antiguedad)
        else: 
            print("Dos o más socio coinciden en antiguedad.")

  


club1=Club()




