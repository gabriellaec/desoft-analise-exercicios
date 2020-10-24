import math
v = float(input("Qual a velocidade: "))
an = int(input("Qual o angulo: "))
g = 9.8
d = (v**2 * math.sin(math.radians(2*an))) / g
if d < 98:
    print("Muito perto")
elif d > 102:
    print("Muito longe")
elif d < 102 and d > 98:
    print("Acertou!")