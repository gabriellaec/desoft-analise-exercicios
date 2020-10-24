import math
def calcula_deistancia_do_proojetil(v,θ,y0)
d=v**2/2*9.8(1+math.sqrt(1+2*9.8*y0/v**2(math.sin(θ))**2)math.sin(2θ)
             return d