import math
def calcula_distancia_do_projetil(v,y,a):
    g = 9.8
    gg = 19.6
    d = a*math.pi/180
    A1 = (math.sin(d))**2
    f1 = (gg*y/(v**2*A1))+1
    f2 = math.sqrt(f1)+1
    A2 = math.sin(2*d)
    f3 = v**2/gg*f2*A2
    return f3