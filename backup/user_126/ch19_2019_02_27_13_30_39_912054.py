import math
def calcula_distancia_do_projetil(v,teta,y0):
    q1=(v**2)/2*9.89
    q2=(1+(2*9.89*y0)/(v**2+math.sin(teta)**2))**0.5
    q3=(1+q2)*math.sin(20)
    d=q1*q3
    return d