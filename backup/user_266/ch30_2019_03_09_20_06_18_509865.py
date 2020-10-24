import math
v = int(input('Velocidade: '))
θ = int(input('Ângulo: '))
d = ((v**2)*math.sin(math.radians(2*θ))/(9.8))
if d > 98 and d < 102:
    print('Acertou!')
elif d > 90 and d < 110:
    print('Muito perto')
else:
    print('Muito longe')
print('{0:.2f}'.format(d))