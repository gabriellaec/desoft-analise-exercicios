def calcula_distancia_do_projetil(v,o,y0,g):
    y=v**2/(2*g)*(1+(1+(2*g*y0)/(v**2*(math.sin(o))**2))*math.sin(2*o)
    return y