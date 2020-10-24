from math import *

g = 9.8
v = float(input("Qual a velocidade da sua jaca? "))
θ = float(input("Qual o angulo de lancamento? "))

d = float((v**2*sin(2*radians(θ)))/g)

if d < 98:
    print('Muito perto')
elif d > 102:
    print('Muito longe')
else:
    print('Acertou!')
    