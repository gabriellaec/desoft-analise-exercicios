def  calcula_distancia_do_projetil(v,a,h):
    d = (v**2/2*9.8)*(1 + math.sqrt(1 + (2*9.8*h)/(v**2*(math.sin(a)**2))))*math.sin(2*a)
    return d