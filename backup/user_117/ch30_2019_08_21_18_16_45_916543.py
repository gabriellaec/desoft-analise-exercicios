import math

v = float(input('velocidade: '))
teta = float(input('angulo: '))  
g = 9.8
d = ((v**2)*math.sin(2*math.radians(teta)))/g

if d - 100 > 2:
    print ('Muito longe')
elif d - 100 < -2:
    print ('Muito perto')
else:
    print ('Acertou!')