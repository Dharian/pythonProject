lista= []
for x in range(5):
    sueldo= int(input("Cual es tu sueldo¿? "))
    lista.append(sueldo)

print("Lista sin ordenar")
print(lista)
for k in range(4):
    for x in range(4):
        if lista[x] < lista[x + 1]:
            aux= lista[x]
            lista[x]=lista[x+1]
            lista[x+1]= aux

print("Lista Ordenada")
print(lista)            