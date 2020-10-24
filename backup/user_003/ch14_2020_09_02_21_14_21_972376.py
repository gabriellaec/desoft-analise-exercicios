import math
def calcula_distancia_do_projetil(v,θ,y0):
    d = ( (v ** 2 ) / 2 * g) * (sin2) * (1 + (1 + (2 * g * y0 ) / (v ** 2 * sin ** 2 ) ) ** 0.5  ) 
    return d
g = float(9.8)
θ = 10
v = 10
y0 = 10
sin = float(math.sin(θ))
sin2 = float(math.sin(θ ** 2))
d = calcula_distancia_do_projetil(v,θ,y0)

print (d)