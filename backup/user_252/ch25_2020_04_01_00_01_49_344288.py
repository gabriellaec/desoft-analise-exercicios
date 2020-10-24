import math
velociade=float(input('qual a velociade: '))
angulo=float(input('qual o angulo: '))
def f(v, a):
    y=(v**2)*(math.sin(math.radians(2*a)))/9.8
    if y<=102 and y>=98:
        print('Acertou!')
    elif y<98 and y>=90:
        print('Muito perto')
    else:
        print('Muito longe')
y=f(velociade, angulo)
print(y)