def calcula_distancia_do_projetil(v,a,y):
    D= [(v**2)/2*9.8]*{1+[2*9.8*y]/v**2*((a))**2}*(2*a)
    return D