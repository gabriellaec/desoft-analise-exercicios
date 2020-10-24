import math
g=9.8
def calcula_distancia_do_projetil(v,o,y):
    x=v**2/(2*g)
    y=1+math.sqrt(1+(2*g*y)/v**2*(math.sin(o)**2))
    z=math.sin(2*o)
    return (x*y*z)
