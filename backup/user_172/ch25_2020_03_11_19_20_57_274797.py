import math
def distancia (v, o):
    d = v**2*math.sin(2*o)/9.8
    return d

if d <98:
    print ('Muito perto')
elif d >102:
    print ('Muito longe')
else:
    print ('Acertou!')