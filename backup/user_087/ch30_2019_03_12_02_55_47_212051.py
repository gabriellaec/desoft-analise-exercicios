import math
def calcula_acerto(v, θ):
    radianos = math.radians(θ)
    d = (v**2)*(math.sin(2*radianos))/9.8
    if d < 98:
        return ('Muito perto')
    elif d > 102:
        return ('Muito longe')
    else:
        return ('Acertou!')
    
    