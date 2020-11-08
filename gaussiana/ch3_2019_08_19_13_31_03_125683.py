import math
def calcula_gaussiana(x,u,o):
 a=1/o*math.sqrt(2*math.pi)
 b=math.exp(-0.5*(((x-u)/o)**2))
 z=a*b
 return z