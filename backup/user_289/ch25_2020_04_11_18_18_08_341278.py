import math
velocidade = float(input('Qual a velocidade da Jaca: '))
angulo = float(input('Qual o ângulo de lançamento da jaca: '))
g = 9.8

d_jaca = (velocidade**2*math.sin(2*math.radians(angulo)))/g

if 98 < d_jaca < 102:
    print("Acertou!")
elif d_jaca > 102:
    print("Muito longe")
else:
    print("Muito perto")
