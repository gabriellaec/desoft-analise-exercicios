import math
v = float(input('Velocidade: '))
θ = float(input('Ângulo: '))
d = (v**2)*math.sin(2*(θ*math.pi/180))/(9.8)
if d>98 and d<102:
    print('Acertou!')
elif d>90 and d<110:
    print('Muito perto')
else:
    print('Muito longe')