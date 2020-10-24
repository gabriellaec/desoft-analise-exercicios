import math
def calcula_distancia_do_projetil(vel,teta,Y0):
    g=9.8
    distancia=((vel**2)/2*g)*(1+(1+(2*g*Y0)/(vel**2)*(math.sin(teta))**2)**(1/2))*(2*math.sin(teta))