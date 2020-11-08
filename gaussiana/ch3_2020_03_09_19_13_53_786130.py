import math 

def calcula_gaussiana(x,μ,σ):
    y=(1/(σ*((2*math.pi)**0.5)))
    a=(math.e**(-0.5*((x-μ)/σ)**2))
    J=y*a
    return J
