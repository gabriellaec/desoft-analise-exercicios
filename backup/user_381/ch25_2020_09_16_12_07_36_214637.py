import math
def distancia(v,θ):
    y = ((v**2)*(math.sin(2*θ)))/(9.8)
    if y < 100:
        print('Muito perto!')
    elif y == 100:
        print('Acertou!')
    else:
        print('Muito longe!')
    return y
