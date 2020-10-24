import math 
v = float(input("Qual a velocidade da Jaca ? "))
t = float(input("Qual o angulo do lançameto ? "))
d = (v**2 * math.sin((4 * math.pi * t)/360))/9.8

if 98 <= d <= 102:
    print("Acertou!")
elif d < 98.0:
    print("Muito perto")
else:
    print("Muito longe")
