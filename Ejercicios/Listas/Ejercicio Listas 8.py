nombres=[]
sueldo=[]
totalsueldos=[]

for x in range(3):
    nombres.append(input("Cual es tu nombre? "))
    mes1=int(input("Cual fue tu sueldo de Junio? "))
    mes2=int(input("Cual fue tu sueldo de Julio? "))
    mes3=int(input("Cual fue tu sueldo de Agosto? "))
    sueldo.append([mes1,mes2,mes3])
    totalsueldos.append(mes1+mes2+mes3)


print(nombres)
print(sueldo)
print(totalsueldos)