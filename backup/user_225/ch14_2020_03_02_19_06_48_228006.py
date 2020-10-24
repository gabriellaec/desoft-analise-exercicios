import math
def calcula_distancia_do_projetil (v, t, y) :
   return(((v**2)/2*9.8)*(1 + (1 + ((2*9.8*y)/((v**2)*(math.sin(t))**2)))**0.5)*math.sin(2*t))