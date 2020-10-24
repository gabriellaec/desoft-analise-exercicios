import math 

v = float(input('Qual a velocidade da jaca? ')) 
a = float(input('Qual o ângulo de lançamento? '))

d = ((v**2)*(math.sin(2*math.radians(a))))/9.8

if d>102:
    print('Muito longe')
elif d<98:
    print('Muito perto')
else:
    print('Acertou!')