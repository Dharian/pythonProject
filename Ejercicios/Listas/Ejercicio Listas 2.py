lista= []

for x in range (5):
    lista.append(input("Ingrese un numero"))
menor=lista[0]
posicion_x=0
for x in range(1,5):
    if lista[x] < menor:
        menor= lista[x]
        posicion_x= x
print("El valor es: ", menor, " y la posicion es: ", posicion_x)