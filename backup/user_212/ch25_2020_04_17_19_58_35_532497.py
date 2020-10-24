import math


v = int(input('insira a velocidade de lançamento'))
a=int(input('insira o ângulo de lançamento da sua jaca'))

g=9.8

d = ((v**2)*(math.sin(2*a)))/g

if d == 98 or d == 102 :
    print ('Muito perto')
if (d>98 and d<102) or d== 100:
    print('Acertou!')
else:
    print ('Muito longe')