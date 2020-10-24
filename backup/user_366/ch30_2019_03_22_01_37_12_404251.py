import math

v = float(input('Velocidade = : '))
x = float(input('Coloque o ângulo (graus): '))

r = x*math.pi*x/180

d = math.sin(2*r)*v**2/9.8

if d >= 98 and d <= 102:
    print('Acertou!')
elif d >= 90 and d <= 110:
    print('Muito perto')
else:
    print('Muito longe')