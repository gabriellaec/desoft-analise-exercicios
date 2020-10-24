import math

def calcula_distancia_do_projetil(v,y0,teta):
    a= (v**2)/2*9.8 
    b= 2*9.8*y0
    c= v**2*(math.sin(2*teta)**2)
    d= a*(1+(1+math.sqrt(b/c)*math.sin(2*teta)
    return (d)
