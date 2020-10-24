import math
velocidade=float(input('Qual é a velocidade?'))
angulo=float(input('Qual o angulo de lançamento?'))
if velocidade**2*math.sin(2*angulo)/9.8>=90 and velociade**2*math.sin(2*angulo)/9.8<=110:
    print('Acertou!')
elif velocidade**2*math.sin(2*angulo)/9.8>=96 and velociade**2*math.sin(2*angulo)/9.8<=104:
    print('Muito perto')
else:
    print('Muito longe')