import math
v=int(input("qual a velocidade"))
o=int(input("qual o angulo"))
g=9.8
x=math.radians(x)
d=((v**2)*math.sin(2*o))/g
if d<98:
    print('Muito perto')
elif d>102:
    print('Muito longe')
else:
    print('Acertou!')