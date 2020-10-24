import math    
g=9.8
v=int(input('velocidade?: '))
angulo=int(input('angulo?: '))
d=((v**2)*math.sin(2*angulo))/g
if (102>=d>=98):
    print ('Acertou')
elif (d<98):
    print ('Muito perto')
else:
    print('Muito longe')