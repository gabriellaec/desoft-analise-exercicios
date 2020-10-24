import math

g = 9.8
v = float(input("Qual a velocidade da jaca? "))
O = float(input("Qual o angulo de lançamento da jaca? "))

d = ((v**2)*math.sin(2*math.radians(O)))/g

if d < 98:
    print('Muito perto')
elif d > 102:
    print('Muito longe')
else:
    print('Acertou!')