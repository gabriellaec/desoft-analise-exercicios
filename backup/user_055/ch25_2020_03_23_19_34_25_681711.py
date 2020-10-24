import math
v = float(input('Velocidade: '))
θ = float(input('Ângulo: '))
d = 100
g = 9.8
def lancamento(v,θ):
    l = ((v**2)*(math.sin(math.radians(2*θ))))/g
    if l > (d-2) and l < (d+2):
        print('Acertou!')
    else:
        if l > (d+2):
            print('Muito longe')
        if l < (d-2):
            print('Muito perto')
lancamento(v,θ)

