import math
v=float(input('qual a velocidade?'))
a=math.radians(int(input('qual o angulo?')))
d=(v**2*math.sin(2*a))/9.8
if d<=98:
    r="muito perto"
elif d>=102:
    r="muito longe"
else:
    r="acertou"
print(r)