def consultarProducto(consulta):
    print(diccionario[consulta])


diccionario={}
for x in range(2):
    clave=str(input("Cual es codigo del producto? "))
    nombre= str(input("Cual es el nombre del producto? "))
    precio= int(input("Cual  es el precio del producto? "))
    cantidad= int(input("Cual  es el cantidad del producto? "))
    diccionario[clave]= (nombre,precio,cantidad)
consulta= str(input("Que producto quieres consultar? "))
consultarProducto(consulta)

print(diccionario)

