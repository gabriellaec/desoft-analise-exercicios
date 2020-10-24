import math

def calcula_distancia_do_projetil(v, θ, y0):
    p1 = v**2/(2*9.8)
    p2 = 2*9.8*y0
    p3 = (v**2*(math.sin(θ)**2))
    y = p1 * (1 + (1 + p2/p3)**0.5) * math.sin(2*θ)
    return y
