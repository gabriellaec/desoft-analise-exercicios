v= input('velocidade: ')
o= input ('angulo: ')
import math
d= ((v**2)* math.sin (2*o))/ 9.8
if d==100:
    print ('Acertou!')
elif d<100:
    print ('Muito perto')
else:
    print ('Muito longe')