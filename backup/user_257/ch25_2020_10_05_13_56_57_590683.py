import math
v = float(input(" Qual a velocidade? "))
a = math.radians(float(input("Qual o angulo? ")))
g = 9.8

d=(v**2*math.sin(math.radians(2*a)))/g
if d < 98:
    print("Muito perto")
elif d > 102:
    print("Muito longe")
else:
    print("Acertou!")
