import math
def calcula_distancia_do_projetil(v,teta,y0):
    raiz=1+math.sqrt(1+((2*g*y0)/(v**2)*(math.sin(teta)**2)))
    d=((v**2)/2*g)*raiz*(math.sin(2*teta))
    return d
