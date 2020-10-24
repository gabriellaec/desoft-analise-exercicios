import math
v = float(input('Velocidade: '))
θ = float(input('Ângulo: '))
g = 9.8
def lancamento(v,θ):
    l = ((v**2)*math.sin(math.radians(2*θ)))/g
    if l > 98 and l < 102:
        print('Acertou!')
    else:
        if l >= 102:
            print('Muito longe')
        if l <= 98:
            print('Muito perto')
lancamento(v,θ)

