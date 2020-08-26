nombre= []
nota = []
for x in range(5):
    notas= int(input("Cual es su Nota¿? "))
    nota.append(notas)
    nombres= str(input("Cual es su nombre ¿? "))
    nombre.append(nombres)


print("Lista sin ordenar")
print(nombre)
print(nota)
for k in range(4):
    for x in range(4):
        if nota[x] > nota[x + 1]:
            aux= nombre[x]
            nombre[x]=nombre[x+1]
            nombre[x+1]= aux
            aux= nota[x]
            nota[x]=nota[x+1]
            nota[x+1]= aux

print("Lista Ordenada")
print(nombre , nota)            
