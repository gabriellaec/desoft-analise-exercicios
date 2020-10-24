import math

v = float(input("Digite a velocidade da jaca: "))
theta = float(input("Digite o ângulo da jaca: "))

d = (v**2*math.sin(2*theta))/9.8

if d<98:
    print("Muito perto")
elif d>102:
    print("Muito longe")
else:
    print("Acertou!")