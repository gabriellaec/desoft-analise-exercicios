import math
def jaca(v, o):
    a = (o/180.0)*math.pi
    d = ((math.sin(2.0*a)*(v**2.0))/9.8)
    if d < 98.0:
        return ('Muito perto')
    elif d >= 98.0 and d <= 102.0:
        return ('Acertou!')
    else:
        return ('Muito longe')
print(jaca(5,30))