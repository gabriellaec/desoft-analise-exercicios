def  calcula_distancia_do_projetil(v, θ, y):
    d = ((v**2)/19.6) * (1 + (1 + (19.6*y / (v**2) * sin(θ)**2)) ** (1/2)
    return d