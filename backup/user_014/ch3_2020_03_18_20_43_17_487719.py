import math
def calcula_gaussiana (x, μ, σ):
    a = (σ * ((2 * math.pi)**1/2))
    c = (((x - μ)/ σ) ** 2)
    d = (1 / a) * math.e ** (-0,5 * c)
    return d

x = 10
μ = 20
σ = 30
print (calcula_gaussiana)

