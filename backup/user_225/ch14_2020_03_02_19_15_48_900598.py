import math
def calcula_distancia_do_projetil (v, t, y) :
   a = ((v**2)/(2*9.8)
   b = (1 + (1 + ((2*9.8*y)/(v**2)*((math.sin(t))**2))
   c = (math.sin(2t)
   return (a*b*c)