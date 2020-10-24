def calcula_distancia_do_projetil (v, g, yo, l,p):
    return (v**2/2*g(1+(2*g*yo/v**2*l)**2)*p)