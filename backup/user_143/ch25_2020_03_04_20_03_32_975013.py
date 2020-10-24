import math
vel= int(input('seu numero:'))
ang= int(input('seu valor:'))
def f(v, b):
    if d>98 and d<102:
        d= (v**2)*math.sin(math.radians(2b))/9.8
        return ('acertou!')
    elif d<=98:
        d= (v**2)*math.sin(math.radians(2b))/9.8
        return ('Muito perto')
    else d>=102:
        d= (v**2)*math.sin(math.radians(2b))/9.8
        return ('Muito longe')
d=f(vel, ang)
print (d)