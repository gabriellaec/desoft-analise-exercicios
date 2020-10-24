import math
def calcula_distancia_do_projetil(v, teta, y):
    g=9.8
    primeira_parte=(v**2)/2*g
    segunda_parte=(1+(1+(2*g*y)/((v*math.sin(teta))**2))**0.5)*math.sin(20)
    final=primeira_parte*segunda_parte
    return final
