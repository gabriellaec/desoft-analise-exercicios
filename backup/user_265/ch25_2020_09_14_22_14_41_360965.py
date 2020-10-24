import math

v = float(input('velocidade'))
a = float(input('angulo'))

d = (v**2) * (math.sin(2 * (a * (math.pi/180)))/9.8
    
if d <= 98:
    print ('Muito perto')
elif d >= 102:
    print ('Muito longe')
else: 
    print ('Acertou!')