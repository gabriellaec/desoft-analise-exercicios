import math
def distancia(v,θ):
    y = ((v**2)*(math.sin(2*θ)))/(9.8)
    if y < 100:
        return 'Muito perto!'
    elif y == 100:
        return 'Acertou!'
    else:
        return 'Muito longe!'
    
