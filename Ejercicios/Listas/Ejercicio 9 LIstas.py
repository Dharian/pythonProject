def cargarLista():
    lista=[]
    for x in range(5):
        lista.append(str(input("Ingresa tus cinco palabras favoritas")))
    print(lista[x])
    comprobarLongitud(lista)

def comprobarLongitud(lista):
    for elemento in lista:
        if len(elemento) > 5:
            print(elemento)
        else:
            print("la palabra ", elemento, " no tiene más de cinco caracteres")


cargarLista()
