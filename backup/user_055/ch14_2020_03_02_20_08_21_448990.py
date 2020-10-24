import math
 def calcula_distancia_do_projetil(v,θ,y0):
     d = ((v**2)/2*g)*(1+(1 + (2*g*y0)/v**2*(sin(θ))**2))**(1/2)*sin(2θ)
     g = 9.8
     return d 