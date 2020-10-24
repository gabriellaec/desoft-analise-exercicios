import math

g = 9.8
v = int(input("Qual a velocidade da jaca? "))
O = int(input("Qual o angulo de lançamento da jaca? "))

d = ((v**2)*math.sin(2*math.radians(O)))/g

if d < 98:
    print('Muito perto')
elif d > 102:
    print('Muito longe')
else:
    print('Acertou!')