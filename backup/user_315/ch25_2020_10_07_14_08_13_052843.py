import math
def f(v, a):
    d=(v**2)*(math.sin(math.radians(2*a)))/9.8
    if d<=102 and d>=98:
        return('Acertou!')
    elif d<98:
        return('Muito perto')
    else:
        return('Muito longe')
    
velociade=float(input('qual a velociade: '))
angulo=float(input('qual o angulo: '))
y=f(velociade, angulo)
print(y)