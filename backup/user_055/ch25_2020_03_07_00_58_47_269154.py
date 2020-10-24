import math
v = int(input('Velocidade: '))
θ = int(input('Ângulo: '))
d = 100
g = 9.8
def lancamento(v,θ,d):
    l = (((v**2)*(math.sin(2*θ)))/g)
    if l >= 98 and l <= 102:
        print('Acertou!')
    if l > 102:
        print('Muito longe')
    if l < 98:
        print('Muito perto')
lancamento(v,θ,d)