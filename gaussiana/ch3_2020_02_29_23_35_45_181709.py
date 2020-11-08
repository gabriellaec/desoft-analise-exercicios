import math
def calcula_gaussiana (x,μ,σ):
    y = 2.718281828459045**(-0.5*(x-μ/σ)**2)/σ*math.sqrt(2*3.14159265359)
print (calcula_gaussiana(3,4,7))
