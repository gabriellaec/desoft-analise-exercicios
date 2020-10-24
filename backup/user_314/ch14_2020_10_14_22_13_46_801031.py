import math

def calcula_distancia_do_projetil(v,angulo,h):
        return (math.exp(v,2)/2*9.8)*math.sin(2*angulo)*(1+math.sqrt(1+ 2*9.8*h/(math.exp(v,2)*math.exp(math.sin(angulo),2))))