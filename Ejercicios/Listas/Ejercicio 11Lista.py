def cargarLista():
    lista=[]
    for x in range(5):
        nombre= str(input("Cual es tu nombre? "))
        lista.append(nombre)
    ordenarLista(lista)    
    imprimirLista(lista)

def ordenarLista(lista):
    lista.sort()
    return lista
          
def imprimirLista(lista):
    print(lista)

cargarLista()