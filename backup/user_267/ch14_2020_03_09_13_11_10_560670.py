def calcula_distancia_do_projetil (v, teta, yo):
    d = (v**2/2*g)*(1 + (2*g*yo/(v**2)*(sin(teta))**2)* sin(2*teta))
    return d