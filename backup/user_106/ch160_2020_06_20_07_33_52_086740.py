import math

def bhask(a):
    sin = 4*a*(180-a) / (40500 - a*(180-a))
    return sin

pior = 0
for x in range(90):
    dif = bhask(x) - math.sin(math.radians(x))
    if abs(dif) > pior:
        pior = abs(dif)
        ponto = x

print(ponto)