import math 
def calcula_gaussiana (x,u,o):
    z = 1/(o*2*math.pi **0.5) 
    k = math.exp(-0,5*(x-u/o)**2)
    calcula_gaussiana = z*k
    return calcula_gaussiana
	