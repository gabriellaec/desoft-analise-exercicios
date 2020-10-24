import math

v=float(input('Qual a velocidade que você quer?'))

a=float(input('Qual angulo você quer?'))
a=math.degrees(a)
g= 9.8

d=((v**2)*math.sin(2*a))/g

print(d)

if d>100:
    print('Muito longe')
elif d<100:
    print('Muito perto')
else:
    print('Acertou!')