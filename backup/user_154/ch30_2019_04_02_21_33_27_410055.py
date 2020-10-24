import math

velocidade = float(input("Velocidade da jaca: "))
th = float(input("Angulo da jaca: "))

distancia = velocidade**2 * math.sin(2*math.radians(th)) / 9.8

if distancia < 98:
    print("Muito perto")
elif distancia > 102:
    print("Muito longe")
else:
    print("Acertou!")