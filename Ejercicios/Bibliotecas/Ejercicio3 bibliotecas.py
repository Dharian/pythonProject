import math


def raiz_Cuadrada(valor):

    resultado = math.sqrt(valor)
    return resultado


def cubo(valor):
    resultado = math.pow(valor, 3)
    return resultado


valor = int(input("Elija un valor: "))
resultado = raiz_Cuadrada(valor)
print(resultado, ": Valor de la raiz cuadrada")
resultado = cubo(valor)
print(resultado, ": Resultado de elevarlo al cubo")
