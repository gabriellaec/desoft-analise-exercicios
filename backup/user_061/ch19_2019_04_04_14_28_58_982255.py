import math
g = 9.8
def calcula_distancia_do_projetil(v,theta,y0):
    o = math.radians(theta)
    if v > 0 and o != 0 and o != math.pi and y0 > 0:
        d = (v**2/2*g)*(1+math.sqrt(1+2*g*y0/((v**2)*((math.sin(o))**2))))*math.sin(o)
        return d