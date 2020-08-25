lista=[]
carga=0
while carga <10:
    lista.append(float(input("Ingrese un valor")))
    carga=carga+1
tamano=len(lista)
print(tamano)
numero=0
while len(lista) != 0:
    numero= numero + lista[0]
    lista.pop(0)
print(numero)
numero=numero/tamano
print(numero, "Despues de la operacion")
print ("El resultado total es : ", numero)