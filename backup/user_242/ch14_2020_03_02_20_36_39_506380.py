import math
g=9.8
def calcula_distancia_do_projetil(v,g,y,t):
    parte1 = v**2/2*9.8*(math.sin(2*t))
    parte2 = 1+(1+2*9.8*y/v**2*(math.sin(t)**2)**1/2
                
    return (parte1*parte2)
                
                