import math
def calcula_gaussiana (x,μ,σ):
    y = 2.7**(-0.5*(x-μ/σ)**2)/σ*math.sqrt(2*math.pi)
print (calcula_gaussiana(10,5,10))
