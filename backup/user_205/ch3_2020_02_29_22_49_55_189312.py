import math
def calcula_gaussiana (x,μ,σ):
    y = e**(-0.5(x-μ/σ)**2)/σ*math.sqrt(2*pi)
print (calcula_gaussiana(3,4,7))
