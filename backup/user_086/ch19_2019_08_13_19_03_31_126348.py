def calcula_distancia_do_projetil(v,θ,yo):
    g=9.8
    d=((v**2)/2*g)*(1+(1+(2*g*yo)/v**2*(math.sin(2*θ)))**1/2)*math.sin(2*θ)
    return d