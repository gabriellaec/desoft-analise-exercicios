import math
def calcula_gaussiana(x,μ,σ):
    a = 1 / (σ * (math.sqrt(2*(math.radians(math.pi))))
    e = math.e**(-0.5*((x-μ/σ)**2))
    f = a*e
    
    return f