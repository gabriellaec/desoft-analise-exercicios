import math
def calcula_distancia_do_projetil(v,y0,g,teta):
    g=9.8
    calcula_distancia_do_projetil=((v)**2/2*g)*(1+(1+(2*g*y0)/((v)**2)))**(1/2)*((math.sin(teta))**2)*(math.sin(2*teta))
    return calcula_distancia_do_projetil