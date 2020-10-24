import math 
v = int(input('velocidade' ))
a = int(input('angulo'))
d = (v**2*math.sin(a))/9.8
if d >98 and d < 102:
    print ('Acertou!')
elif d < 98:
    print ('Muito perto')
else: 
    print ('Muito longe')



