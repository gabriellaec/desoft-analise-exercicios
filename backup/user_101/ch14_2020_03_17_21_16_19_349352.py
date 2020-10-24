import math
def calcula_distancia_do_projetil(v, teta, y):
    g=9.8
    primeira_parte=(v**2)/2*g
    denominador=(v**2)*(math.sin(teta)**2)
    numerador=2*g*y
    raiz=(1+numerador/denominador)**(1/2)
    segunda_parte=(1+raiz)*math.sin(2*teta)
    distancia=primeira_parte*segunda_parte
    return distancia

