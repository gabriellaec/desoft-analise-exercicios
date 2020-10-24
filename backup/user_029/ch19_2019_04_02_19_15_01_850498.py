import math
def calcula_distancia_do_projetil(v,x,z)
     d=v**2/(2*g)*(1+(1+2*g*z/v**2*(math.sin(math.radians(x)))**2)**0.5)*math.sin(2*math.radians(x))
    return d
