import math
def calcula_distancia_do_projetil(v,O,Yo,g=9.8):
	return ((v**2)/(2*g))*(1+math.sqrt(1+(2*g*yo)/(v**2*math.sin(O)**2))*math.sin(2O)