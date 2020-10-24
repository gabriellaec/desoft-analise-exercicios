import math
def calcula_trabalho(F,θ,s):
    T=F*math.cos(math.radians(θ))*s
    return('o valor de T é {} (kg*m**3)/s**2' .format(T))

