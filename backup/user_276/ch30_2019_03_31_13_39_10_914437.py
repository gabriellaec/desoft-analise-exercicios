import math
a = int(input("Ângulo:   "))
b = int(input("Velocidade:   "))
def jaca_wars(v, θ):
    d = ((b**2)/9.8)*math.sin(2*a)
    if d > 98 and d < 102:
    	resultado = 'Acertou!'
    elif d < 98:
        resultado = 'Muito perto'
    else:
        resultado = 'Muito longe'
    return resultado