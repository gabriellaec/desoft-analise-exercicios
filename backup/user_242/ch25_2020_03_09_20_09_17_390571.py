import math
def calcula_distancia_do_projetil(v,theta):
    d = ((v**2) * math.sin (2*theta))/9.8
    if 98 <= d <= 102:
        return 'Acertou!'
    elif d < 98: 
        return 'Muito perto'
    else:
        return 'Muito longe'
