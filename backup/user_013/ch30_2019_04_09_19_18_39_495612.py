import math
# velocidade v
v = float(input())
# angulo A
A = float(input())
# distancia d
d = (v**2)*(math.sin(2*A)) / 9.8

if d < 98:
    print("Muito perto")
elif d <=102:
    print("Acertou!")
else:
    print("Muito longe")
