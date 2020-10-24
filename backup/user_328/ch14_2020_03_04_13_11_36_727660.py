import math


def calcula_distancia_do_projetil(v,y0,teta):
    parte1=((v**2)/2*9.8)
    parte2=(1+math.sqrt(1+(2*9.8*y0)/((v**2)*(math.sin(teta)**2)))
    parte3=(math.sin*(2*teta))
    return(parte1*parte2*parte3)