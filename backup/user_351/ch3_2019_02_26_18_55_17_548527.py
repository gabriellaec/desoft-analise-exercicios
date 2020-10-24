import math
def calcula_gaussiana (x, μ, σ):
    f(x, μ, σ): = 1/(σ*((2*math.pi)**0.5))*(math.e**(-0.5((x-μ)/σ)**2))
    return f(x, μ, σ)
x = 20
μ = 10
σ = 10
print (calcula_gaussiana (x, μ, σ))