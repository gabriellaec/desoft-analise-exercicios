import math
def calcula_distancia_do_projetil(v,t,y0):
    d = v**2/(2*9.8)*(1+(1+(2*9.8*y0)/(v**2*(math.sin(math.radians(t))**2))**0.5))*math.sin(math.radians(2*t))
    return d
print (calcula_distancia_do_projetil(5,20,9))
