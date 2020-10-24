import math
v=float(input())
a=float(input())
d=((v**2)*(math.sin(math.radians(2*a)))/9.8)
if d>102:
    print ('Muito longe')
elif d<98:
    print ('Muito perto')
elif d<=102 and d>=98:
    print('Acertou!')