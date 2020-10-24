from math import sin, radians 
velocidade= float(input('Digite a velocidade de sua jaca: '))
angulo= float(input('Digite o angulo de lancamento de sua jaca: ')) 
g=9.8
d=(velocidade)**2*sin(2*radians(angulo))/g
if d>2:
    print('Sua jaca ficou a {0:.1f} metros, Muito longe'.format(d))
elif d==2:
    print('Sua jaca ficou a {0:.1f} metros,Acertou!'.format(d)) 
else:
    print ('Sua jaca ficou a {0:.0f} metros,Muito perto'.format(d)) 