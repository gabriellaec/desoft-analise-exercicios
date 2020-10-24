import math
def calcula_distancia_do_projetil(v, y, teta):
    la = ((v**2)/19.6)*(1+(1+(19.6*y/(v**2)*(math.radian(math.sin(teta)))**2))**(0.5)*(math.radians(math.sin(teta+teta))))
    return la