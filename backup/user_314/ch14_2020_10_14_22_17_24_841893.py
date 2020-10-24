import math

def calcula_distancia_do_projetil(v,angulo,h):
        a=(math.pow(v,2)/2*9.8)
        b=math.sin(2*angulo)
        c=(1+ math.sqrt(1+ 2*9.8*h/(math.pow(v,2)*math.pow(math.sin(angulo),2))
        
    return a*b*c