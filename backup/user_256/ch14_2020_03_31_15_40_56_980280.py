import math
def calcula_distancia_do_projetil(v, y, teta):
    d = ((v**2)/19.6)*(1+(1+(19.6*y/(v**2)*(math.sin(math.radians(teta)))**2))**(1/2))*math.sin(math.radians(teta*2))
    return d
