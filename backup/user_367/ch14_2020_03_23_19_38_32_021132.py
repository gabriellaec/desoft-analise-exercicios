import math
g = 9.8
def calcula_distancia_do_projetil(v,teta,y0):
    seno=math.sin(2*teta)
    raiz_quociente+(v**2)*(math.sin(teta)**2)
    raiz_numerador=2*g*y0
    raiz=math.sqrt(1+(raiz_numerador/raiz_quociente))
    distancia=((v**2)/(2*g))*(1+raiz)*seno
    return distancia