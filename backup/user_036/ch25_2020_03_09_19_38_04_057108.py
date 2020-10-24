from math import sin
from math import pi

def lancamento(v,a):
    l=(((v**2*(sin(2*a*pi/180))))/9.8)
    if l>102:
        print('Muito longe')
    elif l<98:
        print('Muito perto')
    else:
        print('Acertou!')
        
v1=float(input('Qual a velocidade? '))
a1=float(input('Qual o ângulo de lancamento? '))
lancamento(v1,a1)