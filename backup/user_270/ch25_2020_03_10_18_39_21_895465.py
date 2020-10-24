import math
v = int(input("Diga a velocidade: "))
a = int(input("Diga o angulo: "))

d = (v**2)*math.sin(2*a)/9.8

if d - 100 < 2 or 100 - d < 2 :
    print("Acertou!")
elif 100 - d > 2 :
    print("Muito perto")
else:
    print("Muito longe")