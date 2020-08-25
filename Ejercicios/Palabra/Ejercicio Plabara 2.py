nombre= str(input("Primera palabra "))

letra = nombre[0].lower()

if letra == 'a':
    print("Es vocal, a")
elif letra == 'e':
    print("Es vocal, e")
elif letra == 'o':
    print("Es vocal, o")
elif letra == 'i':
    print("Es vocal, i")
elif letra == 'u':
    print("Es vocal, u")
else:
    print("No empieza por vocal")

