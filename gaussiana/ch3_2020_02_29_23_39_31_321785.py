import math
def calcula_gaussiana (x,μ,σ):
    y = 2.7**(-0.5*(x-μ/σ)**2)/σ*math.sqrt(2*3.14)
print (calcula_gaussiana(0,0,1))
