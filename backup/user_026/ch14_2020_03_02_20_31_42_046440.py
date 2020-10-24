import math

def calcula_distancia_do_projetil (v,y0,teta):
    g=9.8
    p1= (v**2)/(2*g)
    p2= (1+(1+(2*g*y0)/((v**2)*(math.sin*(teta))**2))**(1/2))
    p3= (math.sin*(2*teta))  
    return (p1*p2*p3)

