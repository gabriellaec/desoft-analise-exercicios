def calcula_distancia_do_projetil(v, y0, teta):
    d = ((v**2)/19,6)*(1+(1+(19,6*y0/(v**2)*(sin(teta))**2))**(1/2))
    return d