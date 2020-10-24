import math
v = float(input("Insira a velocidade do lançamento:"))
t = float(input("Insira o ângulo do lançamento:"))
x = (math.pi/180)*t
d = ((v**2)*(math.sin(2*x)))/9.8
if d >= 98 and d <= 102:
    print("Você acertou!")
elif d <= 98:
    print("Muito perto!")
else:
    print("Muito longe!")