import math
def calcula_distancia_do_projetil(v, y0, θ):
    distancia = ((v**2)/2*(9.8))*(1+(1+(2*(9.8)*y0)/((v**2)*(math.sin(θ)**2)**(1/2))*(2*math.sin(θ)*math.cos(θ))))
    return(distancia)