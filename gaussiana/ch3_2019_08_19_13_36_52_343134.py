import math
def calcula_gaussiana(x,u,o):
 a=1/(o*(2*math.pi)**(1/2))
 b=math.exp(-0.5*(((x-u)/o)**2))
 z=a*b
 return z