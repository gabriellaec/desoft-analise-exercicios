import math

def calcula_distancia_do_projetil(v,theta,y0):
    a=(v**2)/(2*9.8)
    b=1+((1+(2*(9.8)*y0)/((v**2)*(math.sin(theta))**2)**(1/2)))
    c=math.sin(2*theta)
    d=(a)*(b)*(c)
    return d