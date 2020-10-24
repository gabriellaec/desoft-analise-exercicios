import math
vel= int(input('seu numero:'))
ang= int(input('seu valor:'))
def f(v, b):
    d= (v**2)*math.sin(math.radians(2*b))/9.8
    if d>98 and d<102:
        return ('acertou!')
    elif d<=98:
        return ('Muito perto')
    else:
        return ('Muito longe')
d=f(vel, ang)
print (d)