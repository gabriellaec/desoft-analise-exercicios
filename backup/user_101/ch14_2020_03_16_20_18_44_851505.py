import math
def calcula_distancia_do_projetil(velocidade, angulo_teta, altura):
    g=9.8
    primeira_parte=(velocidade**2)/2*g
    divisor=(velocidade**2)*(math.sin(angulo_teta))**2
    raiz=(1+((2*g*altura)/divisor)
    distancia=primeira_parte*(1+raiz)*math.sin(20)
    return distancia
