import math
def calcula_gaussiana(x,u,j):
	return (1/(j*math.sqrt(math.pi*2)))**(-0.5*(x-u/j)**2)

print(calcula_gaussiana(0,0,1))
print(calcula_gaussiana(1,3,1))
