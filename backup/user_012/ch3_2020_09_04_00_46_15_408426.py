import math 
def calcula_gaussiana(x, mi, sigma):
    f= (1/(sigma)*0.5*2*3.14)*math.exp(-0.5)*(x - mi/sigma)**2
    return f