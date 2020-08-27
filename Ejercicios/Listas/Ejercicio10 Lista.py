def cargarDatos():
    lista=[]
    for x in range(5):
        valor=int(input("Ingrese un valor "))
        lista.append(valor)
    imprimirLista(set_cero(lista))

def set_cero(lista):
    for x in range(len(lista)):
        if lista[x] < 10:
           lista[x]=0
    return lista

def imprimirLista(lista):
    print(lista)

cargarDatos()