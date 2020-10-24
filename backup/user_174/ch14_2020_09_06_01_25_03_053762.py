def calcula_distancia_do_projetil(v,o,yo):
    d=(v**2/2*g)*(1+(1+2*g*yo/v**2*(sin(o))**2)**(1/2))*sin(2o)
    return d