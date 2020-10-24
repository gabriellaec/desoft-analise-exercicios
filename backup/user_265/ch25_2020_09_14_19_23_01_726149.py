import math
v = int (input('velocidade'))
a = int (input('angulo'))

d = ((v**2) * math.sin * (2 * a * (math.pi/180)))/9.8
    
if d <= 82:
    print ('Acertou!')
elif d >= 82:
    print ('Muito longe')
else: 
    print ('Muito perto')