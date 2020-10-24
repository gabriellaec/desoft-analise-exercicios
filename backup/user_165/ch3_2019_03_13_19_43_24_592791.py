import math
def calcula_gaussiana(x,μ,σ):
	f = ( 1.0 / (σ * math.sqrt(2.0*math.pi)) ) * math.exp(-0.5 * ((x - μ)/ σ)**2)
	return f
#print(calcula_gaussiana(10,10,10))
