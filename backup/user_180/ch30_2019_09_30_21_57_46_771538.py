import math
velocidade = int(input("Velocidade: "))
angulo = int(input("Angulo: "))
d = ((velocidade**2)*(math.sin(math.radians(angulo))))/9.8
if d > 102:
    print("Muito longe")
elif d < 98:
    print("Muito perto")
else:
    print("Acertou!")