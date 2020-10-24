import math
def calcula_distancia_do_projetil(v,θ,yo):
    g = 9.8
    p1 = v**2/(2*g)
    p2 = 1 + (1 + 2*g*yo/(v**2*(math.sin(θ)**2)))**0.5
    p3 = math.sin(2*θ)
    y = p1*p2*p3
    return y