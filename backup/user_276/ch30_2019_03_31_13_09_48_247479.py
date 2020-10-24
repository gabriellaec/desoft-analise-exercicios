import math
def jaca_wars(v, angulo):
    d = ((v**2)/9.8)*math.sin(2*angulo)
    if d > 102:
    	return 'Muito longe'
    elif d < 98:
        return 'Muito perto'
    else:
        return 'Acertou!'