import math

distancia = (int(input("velocidade"))**2*math.sin(2*int(input("TH"))))/9.8

if distancia < 98:
    print("Muito perto")
elif distancia > 102:
    print("Muito longe")
else:
    print("Acertou!")