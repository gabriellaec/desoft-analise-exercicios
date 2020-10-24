import math 
def calcula_gaussiana (x, mi, sigma):
    r=(1/sigma*(2*math.pi)**1/2)
    l=(-0.5*(x-mi/sigma)**2)
    return r**l
print (calcula_gaussiana(0,0,1))
print (calcula_gaussiana (0, (2*math.pi)**-1/2, (2*math.pi)**-1/2))
print (calcula_gaussiana (2,3,1))
