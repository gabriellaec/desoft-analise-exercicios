import math

def calcula_gaussiana(x,mi,sigma):
    
    if sigma==0:
        a=b=0
    elif x==mi:
        a=1/math.sqrt(math.pi*2)
        b=0
        if sigma!=1:
            a=a/sigma
    else:
        a=1/sigma*math.sqrt(math.pi*2)
        b=math.exp(-0.5*((x-mi)/sigma)**2)
        
    y=a*b
    return y
	
   