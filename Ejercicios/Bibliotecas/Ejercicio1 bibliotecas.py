import random

dado1 = random.randint(1, 6)
dado2 = random.randint(1, 6)

print(dado1, dado2)

resultado = dado1 + dado2
print(resultado)
if resultado == 7:
    print("Ganador!")
else:
    print("Pruebe otra vez!")
