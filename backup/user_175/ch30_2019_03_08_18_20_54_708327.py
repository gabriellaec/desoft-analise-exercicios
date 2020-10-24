import math
g = 9.8
a = float(input())
v = float(input())
a = math.radians(a)
d = (v**2)*math.sin(2*a)/g
if (d > 102):
    print('Muito longe')  
elif (d < 98):
    print('Muito perto')  
else:
    print('Acertou!')