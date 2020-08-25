#Excepciones, condicionales.
try:
    edad= int(input("Cual es tu edad?"))
    if edad > 18:
        print ("Tu edad es de :", edad, " y eres mayor de edad")
    elif edad == 0:
        print("Error")
    else:
        print("No eres mayor de edad")
except:
    print("Valor no válido")