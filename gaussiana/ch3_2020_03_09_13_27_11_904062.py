import math
def calcula_gaussiana(x,μ,σ):
	f=(1*e**(-0.5*((x-μ)/σ)**2))/(σ*(2*math.pi)**-1)
	return f
 

