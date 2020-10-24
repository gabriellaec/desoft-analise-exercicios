import math
def calcula_distancia_do_projetil (v, x , y0):
  	A= v**2 / 2 . 9.8
    B= 1 + (1 + 2 * 9.8 * y0 / v**2 (math.sin(x))**2) ** 0.5
    C= math.sin(2 * x)
    x=A*B*C
    return x
	
                        