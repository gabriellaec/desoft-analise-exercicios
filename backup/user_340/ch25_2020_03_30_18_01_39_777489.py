a=int(input('velocidade?'))
b=float(input('angulo?'))
import math
c=math.radians(b)
d=((a**2)*math.sin(2*c))/9.8
if d<100:
    print('Muito perto')
if d==100:
    print('Acertou!')
if d>100:
    print('Muito longe')