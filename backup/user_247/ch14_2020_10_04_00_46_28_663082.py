import math
def calcula_distancia_do_projetil (v, t, y0):
    d1= (v**2)/2*9.8
    d2= (1+(1+(2*9.8*y0))**2)/((v**2)*(math.sin(t))**2)
    d3= (math.sin(t*2))
    y= d1*d2*d3
    return y
    