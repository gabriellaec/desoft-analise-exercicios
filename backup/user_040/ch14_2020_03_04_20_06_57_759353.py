g=9.8
import math
def calcula_distancia_do_projetil(v,teta,y0,g):
    parte1=v*v/(2*g)
    parte2=1+(1+2*g*y0/(v*v*(math.sin(teta))**(1/2))
    parte3=math.sin(2*teta)
    return (parte1*parte2*parte3)