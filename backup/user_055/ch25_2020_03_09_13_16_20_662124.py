import math
v = int(input('Velocidade: '))
θ = int(input('Ângulo: '))
d = 100
g = 9.8
sin_θ = math.sin(math.radians(2*θ))
l = ((v**2)*sin_θ)/g
if l > (d-2) and l < (d+2):
    print('Acertou!')
else:
    if l >= (d+2):
        print('Muito longe')
    if l <= (d-2):
        print('Muito perto')
