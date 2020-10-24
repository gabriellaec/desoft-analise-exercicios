import math
def calcula_distancia_do_projetil(v,θ,h):
    D=((v**2)/(2*9.8))*(1+math.sqrt(1+2*9.8*h/v**2*(math.sin(9.8))**2)*math.sin(2*9.8)
  return D                     