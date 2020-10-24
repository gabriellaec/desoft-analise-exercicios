from math import sin
from math import pi
d=100
def lancamento(v,a):
    l=(((v**2*(sin(2*a*pi/180))))/9.8)
    if l>102:
        print('Muito longe')
    elif l<98:
        print('Muito perto')
    else:
        print('Acertou!')

print(lancamento(44.27,15))