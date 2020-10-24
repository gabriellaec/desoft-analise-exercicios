import math
v = float(input("Velocidade"))
a = float(input("Angulo"))

d = ((v**2) * (math.sin(2*a)))/9.8

if d <= 98:
    print("Muito perto")
else:
    if d >= 102:
        print("Muito longe")
    else:
        print("Acertou!")