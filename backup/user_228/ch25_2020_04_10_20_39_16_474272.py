import math
v=int(input("qual a velocidade?"))
a=int(input("qual o angulo?"))
d=(v**2*math.sin(2*math.radians(a)))/9.8
if d<100:
    print('Muito perto')
elif d>100:
    print('Muito longe')
else:
    print('Acertou!')
      