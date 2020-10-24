import math
def calcula_distancia_do_projetil:
    d = ( (v ** 2 ) / ( 2 * g)) * (1 + math.sqrt(1 + (2 * g * y0 ) / ((v ** 2) * (sin ** 2) ) ) ) * sin2 
    g= 9.8
    sin = float(math.sin(θ))
    sin2 = float(math.sin(θ * 2))
    return d
θ = 10
v = 10
y0 = 10
d = calcula_distancia_do_projetil
