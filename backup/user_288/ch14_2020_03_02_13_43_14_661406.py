import math
def calcula_distancia_do_projetil (v, θ , y0):
  	A= v**2 / 2 * 9.8
    B= (1 + (1 + (2 * 9.8 * y0 / v**2 (math.sin(θ))**2) ** 0.5)
    C= math.sin(2 * θ)
    m=A*B*C
    return m
	
                        