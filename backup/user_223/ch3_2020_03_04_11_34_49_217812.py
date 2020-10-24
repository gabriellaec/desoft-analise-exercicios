import math
def calcula_gaussiana(x, mi, sig):
	cg = ((math.e**(-0.5*((x-mi)/sig)**2))/(sig*(math.sqrt*(2*math.pi)))) 
	return cg
print(calcula_gaussiana(1,2,3))