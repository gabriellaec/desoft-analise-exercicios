import math
def calcula_distancia_do_projetil(v,x,y0):
    distancia = ((v**2)/2*(9.8))*(1+(1+(2*(9.8)*y0)/((v**2)*(math.sin(x)**2)**(1/2))*(2*math.sin(x)*math.cos(x))))
    return(distancia)