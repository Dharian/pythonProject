def cargar_diccionario():
    diccionario={}
    for x in range(5):
        nombre=str(input("Cual es el nombre del producto? "))
        valor=int(input("Cual es el valor del producto? "))
        diccionario[nombre]= valor
    imprimir(diccionario)
    imprimir_mayor100(diccionario)


def imprimir(diccionario):
    print(diccionario)        
    print("diccionario completo impreso")

def imprimir_mayor100(diccionario):
    for x in diccionario:
        if diccionario[x] >= 100:
            print(x,diccionario[x])
        
cargar_diccionario()        