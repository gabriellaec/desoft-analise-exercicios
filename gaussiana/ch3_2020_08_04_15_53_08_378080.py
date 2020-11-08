import math
def calcula_gaussiana(x, u, s):
    Tt=(1/s*(2*math.pi)**1/2)*math.e**(-1/2((x-u)/s)**2)
    return Tt
print (calcula_gaussiana)