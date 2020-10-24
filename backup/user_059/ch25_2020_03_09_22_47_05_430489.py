import math 

v = int(input('Qual a velocidade da jaca? ')) 
a = int(input('Qual o ângulo de lançamento? '))

d = ((v**2)*(math.sin(2*a)))/9.8

if d>102:
    print('Muito longe')
elif d<100:
    print('Muito perto')
else:
    print('Acertou')