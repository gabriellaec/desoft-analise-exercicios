import math
def calcula_distancia_do_projetil(v,theta):
    d = ((v**2) * math.sin (2*theta))/9.8
    if d == 98:
        return 'acertou'
    elif 90 <= d <98 and 99 <= d < 100 :
        return 'muito perto'
    else:
        return 'muito longe'
