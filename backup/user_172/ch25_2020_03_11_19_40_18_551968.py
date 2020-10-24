import math
def distancia (v, o):
    d = v**2*math.sin(2*o)/9.8
    return d
v = int(input('valor de v: '))
o = int(input('valor de o: '))
if distancia(v,o)  < 98:
    print ('Muito perto')
elif distancia(v,o)> 102:
    print ('Muito longe')
else:
    print ('Acertou!')