import math
def calcula_gaussiana (x, μ, σ):
    x != 0
    μ != 0
    return 1/(σ*math.sqrt(2*math.pi))*(math.e)**(-0.5*(x-μ/σ)**2)
    