import math 
v = float(input("Qual a velocidade da Jaca ? "))
t = float(input("Qual o angulo do lançameto ? "))
d = (v**2 * math.sin((4 * math.pi * t)/360))/9.8

if d == 100.0:
    print("Acertou!")
elif d < 100.0:
    print("Muito perto")
else:
    print("Muito longe")
