import math
def calcula_acerto(v, θ):
    alpha = math.pi*θ/180
    d = (v**2)*(math.sin(2*alpha*180/math.pi))/9.8
    if d < 98:
        return ('Muito perto')
    elif d > 102:
        return ('Muito longe')
    else:
        return ('Acertou!')
    
    