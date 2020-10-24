import math
def calcula_distancia_do_projetil(v,t,h):
    g= 9.8
    a= v**2/ 2*g
    b= 1+(1+((2*g*h)/(v**2*(math.sin(t))**2))**(1/2)
    z= math.sin(2*t)

    D= a*b*z 
    return D