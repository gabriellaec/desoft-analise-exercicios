import math
def calcula_gaussiana(x,t,o):
    f=(1/(o*math.sqrt(2*math.pi)))*math.e**((-1/2)*((x-t)/o)**2)
    return f