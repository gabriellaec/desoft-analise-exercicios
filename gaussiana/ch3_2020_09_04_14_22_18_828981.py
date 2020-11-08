import math
def calcula_gaussiana(x,μ,σ):
    gaussiana= (1*math.e**(-0.5*(((x-μ)/σ))**2))/(σ*((2*math.pi)**0.5))
    return gaussiana

a=2
b=3
c=6
print(calcula_gaussiana(a,b,c))
  