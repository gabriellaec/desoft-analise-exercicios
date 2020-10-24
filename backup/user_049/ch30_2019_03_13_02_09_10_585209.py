θ=input('Insira um ângulo: ')
v=input('Insira uma velocidade: ')

import math
def distancia_da_jaca(v,θ):
    d=(v**2*math.sin(2*θ))/9.8
    return d
if 98>=d and 102<=d:
    print ('Acertou!')
elif d<98 and d>102:
    print ('Muito Perto')
else:
    print ('Muito longe')