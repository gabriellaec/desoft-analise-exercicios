import math
def jaca_wars(v, θ):
    d = ((v**2)/9.8)*math.sin(2*θ)
    if d > 102:
    	resultado = 'Muito longe'
    elif d < 98:
        resultado = 'Muito perto'
    else:
        resultado = 'Acertou!'
    return resultado
print(jaca_wars(20,20))