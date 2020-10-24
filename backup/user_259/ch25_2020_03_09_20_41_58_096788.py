import math
v = float(input("Velocidade: "))
t = float(input("Angulo: "))
d=((v**2)*math.sin(math.radians(2*t)))/9.8
if (d-100)<(-2):
    print("Muito perto")     
elif (abs(d-100))<2:
    print("Acertou!")
else:
    print("Muito longe")

