import math

def calcula_gaussiana(x,mi,sigma):
    
    if sigma==0:
        y=0
    else:
        y=(1/sigma*math.sqrt(math.pi*2))*(math.exp(-0.5*((x-mi)/sigma)**2))
        
    return y
	
   