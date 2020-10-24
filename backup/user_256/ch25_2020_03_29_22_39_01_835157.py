import math
def função(v, angulo):    
    d = ((v**2)*math.sin(2*angulo))/9,8
    return d
    if d<98:  
        print('Muito perto')
    if d>102:
        print('Muito longe')
    else:
        print('Acertou!')