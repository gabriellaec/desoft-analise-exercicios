import math

velocidade = int(input("velocidade"))
th = int(input("TH"))

distancia = velocidade**2 * math.sin(2*th) / 9.8

if distancia < 98:
    print("Muito perto")
elif distancia > 102:
    print("Muito longe")
else:
    print("Acertou!")