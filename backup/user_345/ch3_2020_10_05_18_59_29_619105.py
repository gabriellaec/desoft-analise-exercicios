import math
def calcula_gaussiana(x,μ,σ):
     f = (1/(σ*(2*math.pi)**2))*(math.e**(-0.5*(x-μ/σ)**2)
     return f
