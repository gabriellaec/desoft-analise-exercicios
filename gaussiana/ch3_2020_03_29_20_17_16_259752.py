import math
def calcula_gaussiana(x,u,t):
    y = (1/(t*math.sqrt(2*math.pi)))
    z = math.e**(-0.5*((x-u)/t)**2)
   	a = y * z
    return a
 

