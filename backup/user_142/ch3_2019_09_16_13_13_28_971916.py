import math 
def calcula_gaussiana (x,u,o):
	cg = (1/(o*(2*math.pi)))*(math.exp(-0.5*(((x-u)/o)**2)))
	return cg
