import math
def função(v, angulo):    
    la = math.radians(angulo)
    d = ((v**2)*math.sin(la*2))/9,8
    return d
    if d<98:  
        return'Muito perto'
    if d>102:
        return'Muito longe'
    else:
        return'Acertou!'