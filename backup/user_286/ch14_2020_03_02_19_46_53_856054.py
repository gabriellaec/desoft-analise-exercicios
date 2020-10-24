import math

def calcula_distancia_do_projetil(v,y,theta):
    distance = ((v**2)/(2*9.8))*(1 + math.sqrt(1 + (2*9.8*y)/((v**2)*(math.sin(theta)**2))))*math.sin(2*theta)
    return distance