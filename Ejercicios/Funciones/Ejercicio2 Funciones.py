def presentacion():
    numero=0
    
    while numero!=3:
        lista=[]
        print("Bienvenido a la calculadora")
        print("Pulse 1 si quiere sumar")
        print("pulse 2 si quiere restar")
        print("pulse 3 si quiere cerrar la calculadora")
        numero=int(input("Que operacion quiere realizar? "))
        if numero == 1 or numero == 2:
            print("Se necesitan dos numeros")
            lista.append(int(input("Cual es el primer numero? " )))
            lista.append(int(input("Cual es el segundo numero? " )))
            if numero == 1:
               print(sumar(lista))
            else:
               print(restar(lista))
        elif numero == 3:
            despedida()
        else:
            print("El número no es válido")         


def sumar(lista):
    resultado=0
    for c in range(len(lista)):
       resultado= resultado+lista[c]
    return resultado      
        
   

def restar(lista):
   resultado=0   
   if lista[0] > lista[1]:
        resultado=lista[0]-lista[1]
        return resultado
   else:
        resultado= lista[1]- lista[0] 
        return resultado   


def despedida():
   
    print("Adios!!") 

presentacion()        