import math
g=9.8
def distancia(v, teta):
    d=(v**2)*math.sin(math.radians(teta)/g)
    return d
v=int(input('qual a velocidade do projétil? :'))
teta=int(input('qual o angulo de lançamento em relação ao eixo x? :')) 
a=distancia(v, teta)
print('A distancia que o lançamento chegou foi {} metros'.format(a))
if a>=96 and a<=104
    print('Acertou!')
elif a>104:
    print('Muito longe')
else:
    print('Muito perto')