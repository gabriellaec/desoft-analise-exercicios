import math

def calcula_gaussiana(s, m, x):
    gaussiana= 1/(math.sqrt(2*math.pi)*s)*math.exp**(-0.5*(float(x-m)/s)**2)
    return gaussiana