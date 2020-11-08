# -*- coding: utf-8 -*-
import math
def calcula_gaussiana(x,u,j):
	return (1.0/(j*math.sqrt(math.pi*2)))*math.exp((-0.5*((x-u)/j)**2))

print(calcula_gaussiana(0,0,1))
print(calcula_gaussiana(1,3,1))
#print(calcula_gausiana(0, math.sqrt((math.pi))**(-1) ,math.sqrt((math.pi))**(-1))
#print(calcula_gausiana(math.sqrt((math.pi))**(-1) ,math.sqrt((math.pi))**(-1), 0)


