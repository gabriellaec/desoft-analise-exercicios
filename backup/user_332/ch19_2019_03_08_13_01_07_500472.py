import math
def calcula_distancia_do_projetil (v, theta, y0):
    d=((v**2)/2*(9.8))*(1+(1+(2*(9.8)*y0)/((v**2)*(math.sin(theta)**2)**(1/2))*(2*math.sin(theta)*math.cos(theta))
    return(d)