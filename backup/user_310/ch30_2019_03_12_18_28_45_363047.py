import math

v=int(input("velocidade: "))
teta= int(input("angulo: "))

angulo=math.degree(teta)

d= (v**2)*math.sin(angulo*2)/9.8

if d<98:
    print("Muito perto")
elif d>102:
    print("Muito longe")
else:
    print("Acertou!")