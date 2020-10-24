import math
velociade=float(input('qual a velociade: '))
angulo=float(input('qual o angulo: '))
def f(v, a):
    y=(v**2)*(math.sin(math.radians(2*a)))/9.8
    if y<=102 and y>=98:
        return('Acertou!')
    elif y<98:
        return('Muito perto')
    else:
        return('Muito longe')
y=f(velociade, angulo)
print(y)