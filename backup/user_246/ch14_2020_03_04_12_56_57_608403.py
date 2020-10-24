import math
def calcula_distancia_do_projetil(v,o,y):
    x=v**2/(9.8*2)
    y=1+(math.sqrt((1+((2*9.8*y)/(v**2)*((math.sin(o)))**2))))
    z=math.sin(2*o)
    return (x*y*z)
    