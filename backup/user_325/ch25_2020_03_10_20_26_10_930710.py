import math
v = int(input("Velocidade "))
a = int(input("Angulo "))
an = math.degrees(a)
d = ((v**2)*math.sin(2*an))/(9.8)
if d < 98:
    print("Muito perto")
elif d > 102:
    print("Muito longe")
else:
    print("Acertou!")