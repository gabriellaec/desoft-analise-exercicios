import math
def calcula_distancia_do_projeto(v,θ,y0):
    p1=v**2/(2*9.8)
    p2=(1+ math.sqrt(1+(2*9.8*y0)/v**2*(math.sen(θ))**2))
    p3=*math.sin(2*θ)
     m=p1*p2*p3             
    return m                                    