import math
g = 9.8
a = float(input())
v = float(input())
a = math.radians(a)
d = (v**2)*math.sin(2*a)/g
if (distancia < 98):
    print('Muito perto')  
elif (distancia > 102):
    print('Muito longe')  
else:
    print('Acertou!')