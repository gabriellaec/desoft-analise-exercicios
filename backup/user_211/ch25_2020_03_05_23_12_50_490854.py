import math
def dist_da_jaca(v,a):
    d=((v**2)*(math.sin(2*a))/9.8)
    if d>100:
        return 'Muito longe'
    elif d<100:
        return 'Muito perto'
    else:
        return 'Acertou!'