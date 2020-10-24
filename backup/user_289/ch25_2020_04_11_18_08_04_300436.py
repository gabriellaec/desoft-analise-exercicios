import math
velocidade = float(input('Qual a velocidade da Jaca: '))
angulo = float(input('Qual o ângulo de lançamento da jaca: '))
g = 9.8

d_jaca = (velocidade**2*math.sin(2*angulo))/g

if d_jaca == 100:
    print("Acertou")
elif d_jaca > 102:
    print("Muito longe")
else:
    print("Muito perto")
