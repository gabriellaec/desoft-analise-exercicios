import math
def calcula_gaussiana (x,mi,si):
	A=1/(si*(2*math.pi)**(1/2))
	f=A*math.exp(-0.5*((x-mi)/si)**2)
	return f