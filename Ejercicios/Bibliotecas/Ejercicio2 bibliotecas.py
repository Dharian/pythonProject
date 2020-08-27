import random

numero=0
def generarNumero():
    numero=random.randint(1,49)
    print(numero)
    return numero
    


def comprobarNumero(numero):
    valor=0
    veces_probado=0
    while valor!=1:
        numeroUser=int(input("Escoja un número: "))
        if numero > numeroUser:
            veces_probado+=1
            print("El número aleatorio es mayor! ")
        elif numero < numeroUser:
            veces_probado+=1
            print("El numero aleatorio es menor! ")
        else:
            print("Ganaste! ")
            valor=1
            print(veces_probado)

numero=generarNumero()
comprobarNumero(numero)
