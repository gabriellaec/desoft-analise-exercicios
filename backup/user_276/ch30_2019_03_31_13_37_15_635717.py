import math
def jaca_wars(v, θ):
    d = ((v**2)/9.8)*math.sin(2*θ)
    if d > 98 and d < 102:
    	resultado = 'Acertou!'
    elif d < 98:
        resultado = 'Muito perto'
    else:
        resultado = 'Muito longe'
    return resultado

