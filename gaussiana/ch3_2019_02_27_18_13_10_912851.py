import math
def calcula_gaussiana(x,u,j):
	return (1/(j*math.sqrt(math.pi*2)))**(-0.5*(x-u/j)**2)