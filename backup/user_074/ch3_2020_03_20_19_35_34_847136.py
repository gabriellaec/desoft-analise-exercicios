import math
def calcula_gaussiana(x,m,s):
	f=((1/s*(2*math.pi)**1/2)*math.e)**(-1/2((x-m)/s)**2)
	return(f)