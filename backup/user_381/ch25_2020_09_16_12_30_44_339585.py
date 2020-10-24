import math
def distancia(v,θ):
    y = ((v**2)*(math.sin(math.radians(2*θ))))/(9.8)
    if y < 98:
        print('Muito perto!')
    elif y >= 98 and y <= 102:
        print('Acertou!')
    else:
        print('Muito longe!')
    return y 
    
