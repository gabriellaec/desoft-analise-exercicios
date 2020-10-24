def calcula_distancia_do_projetil(v,θ,y):
    y=(v**2/2*g)*(1+(1+2*g*y/v**2*(sin(θ))**2)**0.5)*sin(2*θ)
    return y