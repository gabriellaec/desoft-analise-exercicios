import math

sin = math.sin
degrees = math.degrees
radians = math.radians

distância = ((velocidade ** 2) * (sin(radians((2*ângulo))) / 9.8))

if distância <= 98:
    print("Muito perto")
    print(distância)

elif distância >= 102:
    print("Muito longe")
    print(distância)
else:
    print("Acertou")
    print(distância)