import math
v = int(input("Diga a velocidade: "))
a = int(input("Diga o angulo: "))

d = (v**2)*math.sin(2*a)/9.8

if d >= 98 and d <= 102 :
    print("Acertou!")
elif d < 98 :
    print("Muito perto")
else:
    print("Muito longe")