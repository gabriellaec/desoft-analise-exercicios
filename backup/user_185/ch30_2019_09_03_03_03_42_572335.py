import math

sin = math.sin
degrees = math.degrees

distância = ((velocidade ** 2) * (sin(degrees(2*ângulo)) / 9.8))

if distância <= 98:
    print("Muito perto")

elif distância >= 102:
    print("Muito longe")
else:
    print("Acertou")