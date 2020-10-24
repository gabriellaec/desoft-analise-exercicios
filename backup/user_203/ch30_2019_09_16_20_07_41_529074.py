from math import sin, radians 
velocidade= float(input('Digite a velocidade de sua jaca '))
angulo= float(input('Digite o angulo de lancamento de sua jaca ')) 
g=9.8
d=(velocidade)**2*sin(2*angulo)/g
if d>2:
    print('Muito longe')
elif d==2:
    print('Acertou!') 
else:
    print ('Muito perto') 