from math import sin
def calcula_distancia_do_projetil(v, a, yo):
    d = ((v**2)/2*(9.8))*(1+(1+(2*9.8*yo)/((v**2)*((sin(a))**2)))**(1/2)*sin(2*a))
    return d