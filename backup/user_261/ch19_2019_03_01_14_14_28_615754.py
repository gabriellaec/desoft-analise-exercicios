import math
def calcula_distancia_do_projeto(v,θ,y0):
    y= v**2/(2*9.8)*(1+ math.sqrt(1+((2*9.8*y0)/v**2*(math.sen(θ))**2)*math.sin(2*θ)
    return y                                     