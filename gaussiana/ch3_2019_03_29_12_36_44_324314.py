import math
def calcula_gaussiana(x, mi, sig):
	gauss= (1/mi*math.sqrt(2*math.pi))*exp(-0.5*(((x-mi)/sig)**2))
	return gauss