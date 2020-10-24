import math

def calcula_distancia_do_projetil(v,g,y,teta):
    return v**2/2*9.8*(1+(1+(2*g*y/((v**2)*(math.sin(teta)**2)**(1/2)))))*math.sin(2*teta)