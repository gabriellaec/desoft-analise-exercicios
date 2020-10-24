import math
import math
def jacawars(v,angulo):
    convert = math.radians(2*angulo)
    d = v**2*(math.sin(convert))/9.8
    if d>=98 and d<102:
        return 'Acertou!'
    if d<98:
        return'Muito perto'
    if d>102:
        return 'Muito longe'
a = float(input('digite sua velocidade'))
b = float(input('digite seu angulo'))
x = jacawars(a,b)
print(x)