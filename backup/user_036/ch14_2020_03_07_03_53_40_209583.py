import math
d=100
def lancamento(v,a):
    l=(((v**2*math.sin(2*a)))/9.8)
    if l >= 98 and l <= 102:
        print('Acertou!')
    if l>102:
        print('Muito longe')
    if l<98:
        print('Muito perto')

input(lancamento(33,45))