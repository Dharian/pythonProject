lista_nombre= []
lista_edad= []

for x in range(5):
    lista_nombre.append(input("Cual es tu nombre? "))
    lista_edad.append(int(input("Cual es tu edad? ")))

for x in range(5):
    if lista_edad[x] >= 18:
        print("Mi nombre es: ", lista_nombre[x]," y mi edad es: ", lista_edad[x])
   

