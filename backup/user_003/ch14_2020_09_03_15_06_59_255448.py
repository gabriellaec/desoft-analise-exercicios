import math
def calcula_distancia_do_projetil(v,θ,y0):
    d = ( (v ** 2 ) / 2 * g) * (1 + math.sqrt(1 + (2 * g * y0 ) / (v ** 2 * math.sin(θ) ** 2 ) ) ) * math.sin(θ * 2)  
    return d
g = 9.8
θ = 10
v = 10
y0 = 10
d = calcula_distancia_do_projetil(v,θ,y0)
