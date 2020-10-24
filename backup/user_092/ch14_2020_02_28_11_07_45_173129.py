import math
def calcula_distancia_do_projetil(v,y,θ):
    θ = math.radians(θ)
    return((v**2/19.6)*(1+(math.sqrt(1+((19.6*y)/(v**2*(math.sin(θ))**2)))))*(math.sin(2*θ)))