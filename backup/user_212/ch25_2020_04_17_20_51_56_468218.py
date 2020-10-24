from math import sin, radians 


v = float(input('insira a velocidade de lançamento'))
a=float(input('insira o ângulo de lançamento da sua jaca'))

g=9.8

d = ((v**2)*sin(radians(2*a)))/g

if d < 98:
    print ('Muito perto')
if (d=>98 and d<=102) or d== 100:
    print('Acertou!')
else:
    print ('Muito longe')