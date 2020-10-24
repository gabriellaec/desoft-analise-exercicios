import math

velocidade = float(input("Velocidade da Jaca: "))
theta = float(input("Angulo: "))

distancia = velocidade ** 2 * math.sin(2 * math.radians(theta)) / 9.8

if distancia < 98:
    print("Muito perto")
elif distancia > 102:
    print("Muito longe")
else:
    print("Acertou!")