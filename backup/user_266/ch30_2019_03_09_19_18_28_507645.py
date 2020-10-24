import math
v = int(input('Velocidade: '))
θ = int(input('Ângulo: '))
a = (math.pi*θ/90)
d = ((v**2)*math.sin(2*a)/(9.8))
if d > 98 and d < 102:
    print('Acertou!')
elif d > 90 and d < 110:
    print('Muito perto')
else:
    print('Muito longe')
print('{0:.2f}'.format(d))