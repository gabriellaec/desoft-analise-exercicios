import math
def calcula_gaussiana(x,m,s):
	a=s*(2*math.pi)**0.5
	b=math.e
	c=-0.5*((x-m)/s)**2
	y=(1/a)*b**c
	return y