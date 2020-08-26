def presentacion():
    numero=0
    while numero!=3:
        print("Bienvenido a la calculadora")
        print("Pulse 1 si quiere sumar")
        print("pulse 2 si quiere restar")
        print("pulse 3 si quiere cerrar la calculadora")
        numero=int(input("Que operacion quiere realizar? "))
        if numero == 1 or numero == 2:
            print("Se necesitan dos numeros")
            num1=int(input("Cual es el primer numero? " ))
            num2=int(input("Cual es el segundo numero? " ))
            if numero == 1:
                sumar(num1, num2)
            else:
                restar(num1, num2)    
        elif numero == 3:
            despedida()
        else:
            print("El número no es válido")         


def sumar(num1, num2):
    resultado= num1 + num2
    print(resultado)     
   

def restar(num1,num2):
    if num1 > num2:
        resultado= num1 - num2
        print(resultado)
    else:
        resultado=num2-num1
        print(resultado)


def despedida():
   
    print("Adios!!") 

presentacion()        