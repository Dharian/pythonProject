lista=[]
numero = 1

while numero != "0":
    numero= input(" Ingresa un numero. Para terminar escribe un 0. ")
    if numero != "0":
        lista.append(numero)
    else:
        print(len(lista))

