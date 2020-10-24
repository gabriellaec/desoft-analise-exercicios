import math
def calcula_distancia_do_projetil(v,y0,ang):
    a= (v**2)/(2*9.8)
    b= 2*9.8*y0
    c= v**2 *(math.sin(ang))**2
    d= math.sin(2*ang)
    form= a * (1+(1+b/c)**(1/2))*d
    return form