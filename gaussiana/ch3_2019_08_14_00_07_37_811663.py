import math
def calcula_gaussiana(x,mi,sigma):
	y=(1/sigma*(2*math.pi)**(1/2))*(-0.5((x-mi)/sigma)**2)
	return y
a = 1
b = 2
c = 3
d = calcula_gaussiana(a,b,c)

print (d)