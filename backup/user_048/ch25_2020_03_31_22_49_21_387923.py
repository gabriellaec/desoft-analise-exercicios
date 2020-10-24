g=9.8
import math
def calcula(v,o):
    d=((v**2)*math.sin(2*o))/g
    if d<98:
            return('Muito perto')
    elif 102<d:
            return('Muito longe')
    else:
            return('Acertou!')