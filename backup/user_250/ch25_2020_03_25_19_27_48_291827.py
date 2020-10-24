import math

v = float(input("Digite a velocidade da jaca: "))
theta = float(input("Digite o ângulo da jaca: "))

d = (v**2*math.sin(2*theta))/9.8

if d>102:
    print("Muito longe")
if d<98:
    print("Muito perto")
else:
    print("Acertou!")