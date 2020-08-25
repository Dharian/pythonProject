numero1 = int(input("Primer Numero"))
numero2 = int(input("Segundo Numero"))
numero3 = int(input("Tercer Numero"))
total= (numero1+numero2+numero3)/3

if total > 7:
    print ("Promocionado")
    print(total)
elif total >= 4 and total< 7:
    print("Regular")
    print(total)
elif total <4:
    print("Suspenso")
    print(total)
else:
    print("Algo ha ido mal")
    print(total)
