import math
v=float(input('qual a velocidade?'))
a=math.radians(int(input('qual o angulo?')))
g=9.8
d=((v**2)*math.sin(2*a))/g
if d<98:
    r="Muito perto"
elif d>102:
    r="Muito longe"
else:
    r="Acertou!"
print(r)