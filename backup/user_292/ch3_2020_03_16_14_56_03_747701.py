import math
def calcula_gaussiana (x,μ,σ):
    a=σ*math.sqrt(2*math.pi)
    b=(-0.5)*((x-μ)/σ)**2
    f=math.exp(b)/a
    return f

