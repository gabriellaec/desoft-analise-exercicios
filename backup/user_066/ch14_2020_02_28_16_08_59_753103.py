import math
def calcula_distancia_do_projetil(v, teta, yo):
    d =(v**2/2*9.8)*(1+(1+(2*9.8*yo)/((v**2)*(sin(teta*math.pi/180))*2)*(1/2))*sin(teta*math.pi*90)
    return d