import math
def calcula_gaussiana (x, u, o):
	a=(1/o*(math.sqrt(2*math.pi)))
    b=math.e**(-0.5*((x-u)/o)**2)
    f=a*b
    return f

 
 

