import math
v=int(input('qual a velocidade?'))
a=int(input('qual o angulo?'))
d=(v**2*math.sin(2*a))/9.8
if d<99:
    r="muito perto"
elif d>101:
    r="muito longe"
else:
    r="acertou"
print(r)