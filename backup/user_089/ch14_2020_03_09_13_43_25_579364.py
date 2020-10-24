import math
def calcula_distancia_do_projetil(v,t,h):
    g= 9.8
    a= (int(v**2/ 2*g))
    b=(int(1+(1+((2*g*h)/(v**2*(math.sin(t))**2))**(1/2)))
    c= (int(math.sin(2*t)))

    D= a*b*c 
    return D