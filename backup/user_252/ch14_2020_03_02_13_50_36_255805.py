import math
def calcula_deistancia_do_proojetil(v,θ,y0)
g=9.8
d=((v**2)/(2*g))*(1+math.sqrt(1+(2*g*y0/v**2*(math.sinθ))**2)*(math.sin(math.degrees2*θ)))
             return d