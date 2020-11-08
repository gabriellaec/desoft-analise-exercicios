import math

def calcula_gaussiana(x,μ,σ):
    x = -0.5((( x - μ ) / σ ) ** 2)
    f = 1 / ( σ * ( math.sqrt( 2 * math.pi))) * math.exp(x)
    return f