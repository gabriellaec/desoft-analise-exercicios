import math
def calcula_gaussiana(x, mu, sig):
    
    if (sig > 0):
    	f = (1/(sig*math.sqrt(2*pi)))*e^(-0.5*((x-mu)/sig)^2)
    
    	return f