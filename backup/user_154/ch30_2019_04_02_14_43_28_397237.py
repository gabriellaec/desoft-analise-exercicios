import math

velocidade = float(input("Speed"))
th = float(input("TH"))

distancia = (v**2*math.sin(2*th))/9.8

if distancia < 98:
    print("Muito perto")
elif distancia > 102:
    print("Muito longe")
else:
    print("Acertou!")