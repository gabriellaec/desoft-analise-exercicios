import math

def calcula_distancia_do_projetil(v, θ, y0):
    distância1 = ((v**2)/((2*9.8)))*(1+(1+(2*9.8*y0)/(v**2*(math.sin(θ))**2))**(1/2))*math.sin(2*θ)
    distância2 = (1+(1+(2*9.8*y0)/(v**2*(math.sin(θ))**2))**(1/2))
    distância3 = math.sin(2*θ)
    return distância1*distância2*distância3