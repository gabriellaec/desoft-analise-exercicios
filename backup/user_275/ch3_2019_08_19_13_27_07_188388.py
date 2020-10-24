import math
def calcula_gaussiana(x,u,o):
 a=1/o*math.sqrt(2*math.pi)
 b=math.e
 c=-0.5*((x-u)/o)**2
 z=a*(b**c)
 return z