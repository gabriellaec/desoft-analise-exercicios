
import math

def calcula_distancia_do_projetil(v,t,y):
    d=(v*v*math.sin(2*t)/19.6)*(1+math.sqrt(1+(19.6*y/(v*v*math.sin(t)*math.sin(t)))))
    return d