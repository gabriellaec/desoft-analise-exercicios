import math
def calcula_distancia_do_projetil(v, y0, teta):
    la = ((v**2)/19.6)*(1+(1+(19.6*y0/((v**2)*(math.sin(math.radians(teta)))**2)))**(0.5)*(math.sin(math.radian(teta*2))))
    return la