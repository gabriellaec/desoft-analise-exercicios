import math

def calcula_distancia_do_projetil(v, ang, alt):
    d = ((v**2)/(2*9.8))*(1+(math.sqrt(1+(2*9.8*alt)/((v**2)*(math.sin(ang)**2)))*math.sin(2*ang)
    return d