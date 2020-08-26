def sumar(var1, var2 , *lista):
    resultado= var1+ var2
    for x in range(len(lista)):
        resultado=resultado+ lista[x]
    print(resultado)    

def presentacion():
    print("--------")
    var1= int(input("Primer numero: "))
    var2= int(input("Segundo numero: "))
    var3= int(input("Tercer numero: "))
    var4= int(input("Cuarto numero: "))
    sumar(var1,var2,var3,var4)

presentacion()
                