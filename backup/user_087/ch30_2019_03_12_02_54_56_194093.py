import math
def calcula_acerto(v, θ):
    radianos = math.radians(θ)
    d = (v**2)*(math.sin(2*radianos))/9.8
    if d > 102:
        return ('Muito longe')
    elif d < 98:
        return ('Muito perto')
    else:
        return ('Acertou!')
    
    