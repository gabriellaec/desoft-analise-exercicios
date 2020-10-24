import math
def calcula_distancia_do_projetil(v,t,y0,g):
    d = v**2/(2*g)*(1+math.sqrt(1+(2*g*y0)/(v**2*(math.sin(math.radians(t))**2))))*math.sin(math.radians(2*t))
    return d
print (calcula_distancia_do_projetil(5,20,9,9.8))
