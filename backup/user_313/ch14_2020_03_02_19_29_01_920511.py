import math

def calcula_distancia_do_projetil (v,y,theta):
    parte1 = ((v**2)/(2*9.8))
    parte2 = ((1+(math.sqrt(1+(2*9.8*y))/((v**2)*(math.sin(theta)**2)))))
    parte3 = math.sin(2*theta)

    return(parte1*parte2*parte3)