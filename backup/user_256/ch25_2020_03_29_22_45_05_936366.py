import math
def função(v, angulo):    
    d = ((v**2)*math.sin(2*angulo))/9,8
    if d<98:  
        return'Muito perto'
    if d>102:
        return'Muito longe'
    else:
        return'Acertou!'