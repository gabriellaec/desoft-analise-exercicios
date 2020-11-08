import math
def calcula_gaussiana(x,μ,σ):
    a= 1/(σ*((2*math.pi)**0.5))
    b= ((x-μ)/σ)**2
    result= a*10**((-0.5)*b)
    return result