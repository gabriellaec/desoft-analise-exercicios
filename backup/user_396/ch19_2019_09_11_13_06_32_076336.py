g = 9.8
def  calcula_distancia_do_projetil(v, θ, y):
    d = ((v**2)/(2*g)) * (1 + (1 + ((2*g)*y / (v**2) * sin(θ)**2))** (1/2)) * sin(2*θ)
    return d