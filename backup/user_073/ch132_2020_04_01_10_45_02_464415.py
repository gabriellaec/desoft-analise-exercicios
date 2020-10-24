import math
def calcula_trabalho(F,θ, s,tempo):
    t= F*math.degrees(math.cos(θ))*s
    J=t*((F*1000*s**2)/tempo)
    return J
