import math
def calcula_distancia_do_projetil(v, angulo, y0):
    distancia = ((v**2)/2*(9.8))*(1+(1+(2*(9.8)*y0)/((v**2)*(math.sin(math.degrees(angulo))**2)**(1/2))*(2*math.sin(math.degrees(angulo))*math.cos(math.degrees(angulo)))))
    return(distancia)