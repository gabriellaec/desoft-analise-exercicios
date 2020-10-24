import math
def calcula_trabalho(F,θ,s):
    T=F*math.cos(math.radians(θ))*s
    return(' {} (kgm^3)/s^2'.format(T))

