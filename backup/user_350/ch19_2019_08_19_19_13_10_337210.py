from math import sqrt
from math import sin
def calcula_distancia_do_projetil(v,t,y):
    g=9.8
    temp1= (v**2)/(2*g)
    temp2= (1+ sqrt(1 + (2*g*y)/((v**2)*(sin(t))**2)
    temp3= sin(2t)
    return temp1*temp2*temp3
                    
                  
    
   