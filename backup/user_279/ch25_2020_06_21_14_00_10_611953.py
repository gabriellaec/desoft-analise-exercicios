import math
v = int(input("Qual a velocidade: "))
an = int(input("Qual o angulo: "))
g = 9.8
d = (v**2 * math.sin(2*an)) / g
if d < 98:
    print("Muito perto")
if d > 102:
    print("Muito longe")
else:
    print("Acertou!")