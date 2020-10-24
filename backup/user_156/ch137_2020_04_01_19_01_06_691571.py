import math

def calcula_aceleracao(r, f):
    omega = 2*math.pi*(f/60)
    aceleracao_centripeta = (omega**2)*r
    
    return aceleracao_centripeta