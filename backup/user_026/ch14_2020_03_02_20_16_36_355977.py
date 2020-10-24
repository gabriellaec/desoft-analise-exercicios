import math

def calcula_distancia_do_projetil (v,y0,teta):
    g=9.8
    parte1=(v**2)/(2*g)
    parte2= 1+(1+(2*g*y0)/(v**2)*(math.sin*teta)**2)
    parte3= math.sin*(2*teta)
    d=(parte1*parte2*parte3)
    return (d)
    