import math
def distancia(v,θ):
    y = ((v**2)*(math.sin(math.radians(2*θ))))/(9.8)
    if y < 98:
        resultado = 'Muito perto!'
    elif y >= 98 and y <= 102:
        resultado = 'Acertou!'
    else:
        resultado = 'Muito longe!'
    return resultado 
    
