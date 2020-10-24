import math
def calcula_distancia_do_projetil(v, y, teta):
    la=math.radians(teta)
    d = ((v**2)/19.6)*(1+(1+(19.6*y/(v**2)*(math.sin(la))**2))**(1/2))*math.sin(2*la)
    return d
