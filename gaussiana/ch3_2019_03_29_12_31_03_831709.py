import math
def calcula_gaussiana(x, mi, sig):
	gauss=(1/sig*(2*math.pi)**(1/2))*math.exp(-0.5*((x-mi)/sig)**3)
	return gauss