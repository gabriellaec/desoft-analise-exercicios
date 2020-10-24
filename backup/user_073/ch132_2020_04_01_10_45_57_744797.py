import math
def calcula_trabalho(F,θ,s):
    t= F*math.degrees(math.cos(θ))*s
    J=t*((F*1000*s**2)/tempo**2)
    return J
