import math
v = int(input("Insira a velocidade do lançamento:"))
t = int(input("Insira o ângulo do lançamento:"))
d = (v**2)*(math.sin(2*t/math.pi))/9.8
if d > 98 and d < 102:
    print("Você acertou!")
elif d < 98:
    print("Muito perto!")
else:
    print("Muito longe!")