import math
g = 9.8
v = float(input('valor da velocidade:'))
θ = float(input('valor do ângulo:'))
d = ((v**2)*math.sin(2*math.radians(θ)))/g
if d == 100:
    print('Acertou!')
elif d < 100:
    print('Muito perto')
else:
    print('Muito longe')