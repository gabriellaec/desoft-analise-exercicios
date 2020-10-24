a=int(input('velocidade?'))
b=float(input('angulo?'))
import math
c=math.radians(b)
d=((a**2)*math.sin(2*c))/9.8
if d<98:
    print('Muito perto')
if d==98 and d==102:
    print('Acertou!')
if d>102:
    print('Muito longe')