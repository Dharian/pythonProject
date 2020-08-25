nombre= input("Ingresa tu correo")
cantidad=0
tamano = len(nombre)
i=0
while i != tamano:
    if nombre[i] != "@":
        print("")
    else:
        print("@")
        cantidad= cantidad+1
    i = i + 1

if cantidad == 1:
    print("Correo válido")
else:
    print("El correo no es valido.")


if nombre.count("@") < 2:
    print("true")
else:
    print("false")