import math

def calcula_distancia_do_projetil (v,y0,teta):
  
    p1=(v**2/(2*9.8))
    p2=(1+math.sqrt(1+(2*9.8*y0)/((v**2)*(math.sin(teta)**2))))
    p3=(math.sin(2*teta))
    return (p1*p2*p3)


    

