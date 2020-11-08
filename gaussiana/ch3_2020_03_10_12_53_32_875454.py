import math 
def calcula_gaussiana(x,y,z):
	w=1/(z*(2*math.pi)**(1/2))
	t=math.e**(-0.5*((x-y)/z)**2)
	h=w*t
	return h