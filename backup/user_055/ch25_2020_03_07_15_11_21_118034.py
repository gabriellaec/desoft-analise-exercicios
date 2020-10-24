import math
v = int(input('Velocidade: '))
θ = int(input('Ângulo: '))
d = 100
g = 9.8
def lancamento(v,θ):
    l = ((v**2)*math.sin(2*θ))/g
    if l > (d-2) and l < (d+2):
        print('Acertou!')
    else:
        if l >= (d+2):
            print('Muito longe')
        if l <= (d-2):
            print('Muito perto')
    return l
lancamento(v,θ)
