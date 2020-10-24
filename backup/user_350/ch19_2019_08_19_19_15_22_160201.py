from math import sqrt
from math import sin
def calcula_distancia_do_projetil(v,t,y):
    g=9.8
    tmp1= (v**2)/(2*g)
    tmp2= (1+ sqrt(1 + (2*g*y)))/((v**2)*(sin(t))**2)
    tmp3= sin(2*t)
    return tmp1*tmp2*tmp3
                    
                  
    
   