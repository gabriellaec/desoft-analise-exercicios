
import math
d=100
def lancamento(v,a):
    l=(((v**2*math.sin(2*a)))/9.8)
    if l>102:
        print('Muito longe')
    elif l<98:
        print('Muito perto')
    else:
        print('Acertou!')

print(lancamento(33,45))