class Persona:

    def inicializar(self, nom, ed):
        self.nombre = nom
        self.edad = ed

    def imprimirNombre(self):
        print(self.nombre)

    def imprimirEdad(self):
        print(self.edad)

    def comprobarEdad(self):
        if self.edad >= 18:
            print(self.nombre, " es mayor de edad")
        else:
            print(self.nombre, " es menor de edad")

persona1=Persona()
persona1.inicializar("Pepe",18)
persona1.imprimirEdad()
persona1.imprimirNombre()
persona1.comprobarEdad()

persona2=Persona()
persona2.inicializar("Pablo",17)
persona2.imprimirEdad()
persona2.imprimirNombre()
persona2.comprobarEdad()