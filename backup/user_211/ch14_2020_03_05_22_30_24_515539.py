import math
def calcula_distancia_do_projetil(v,teta,alt):
     dist=(v**2/2*9.8)*(1+math.sqrt(1+((2*9.8*alt)/((v**2)*(math.sin(teta)**2)))
	return dist