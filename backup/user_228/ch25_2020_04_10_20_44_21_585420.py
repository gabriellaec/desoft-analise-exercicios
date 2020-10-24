import math
v=float(input("qual a velocidade?"))
a=math.radians(float(input("qual o angulo?")))
d=(v**2*math.sin(2*a))/9.8
if d<98:
    print('Muito perto')
elif d>102:
    print('Muito longe')
else:
    print('Acertou!')
      