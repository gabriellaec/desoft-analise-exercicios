import math
def calcula_distancia_do_projetil(v,theta,y0):
    g = 9.8 
    f1 = v**2/2*g
    f2 = 1 + (math.sqrt(1 + ((2*g*y0)/(v*v*math.sin(theta)*math.sin(theta))
    f3 = math.sin(2*theta)

    d = f1*f2*f3

    return d