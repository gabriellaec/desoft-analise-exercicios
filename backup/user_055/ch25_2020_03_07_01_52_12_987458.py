import math
v = int(input('Velocidade: '))
θ = int(input('Ângulo: '))
d = 100
g = 9.8
def lancamento(v,θ,d):
    l = (((v**2)*(math.sin(2*θ)))/g)
    if l > (d-2) and l < (d+2):
        print('Acertou!')
    if l > (d+2):
        print('Muito longe')
    if l < (d-2):
        print('Muito perto')
if θ >= 0 and θ <= 90:
    lancamento(v,θ,d)
    