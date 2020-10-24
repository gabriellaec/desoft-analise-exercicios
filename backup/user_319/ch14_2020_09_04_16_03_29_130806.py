import math
def calcula_distancia_do_projetil(v,teta,yo):
    d=(v**2/2*g)*(1+(1+(2*g*yo)/v**2*(math.sin(teta))**2)**(1/2))*math.sin(2*teta)
    return d