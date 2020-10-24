import math
def jaca(v, o):
    a = (o/180.0)*math.pi
    d = (((v**2.0)*math.sin(2.0*a))/9.8)
    if d < 98.0:
        return ('Muito perto')
    elif d >= 98.0 and d <= 102.0:
        return ('Acertou!')
    else:
        return ('Muito longe')
v = float(input("velocidade"))
o = float(input("angulo"))