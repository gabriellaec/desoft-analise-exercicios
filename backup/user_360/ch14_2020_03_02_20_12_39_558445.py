import math

def calcula_distancia_do_projetil(v,y0,teta):
    projetil1= (v**2)/(2*98/10) * (math.sin(2*teta))
    projetil2= (1+ 1+(2*9.8*y0/v**2*(math.sinteta**2))**1/2)
    return(projetil1*projetil2)