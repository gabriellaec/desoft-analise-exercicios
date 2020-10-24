def calcula_distancia_do_projetil(x,y,z):
    g=9.8
    d=x**2/g*2(1+(1+2g*z/x**2(sin(y))**2)**-1)*sin(2*y)
    return d