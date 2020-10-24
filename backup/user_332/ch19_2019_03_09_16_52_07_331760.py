import math
def calcula_distancia_do_projetil(angulo, y0, v):
    distancia = ((v**2)/2*(9.8))*(1+(1+(2*(9.8)*y0)/((v**2)*(math.sin(angulo)**2)**(1/2))*(2*math.sin(angulo)*math.cos(angulo))))
    return(distancia)