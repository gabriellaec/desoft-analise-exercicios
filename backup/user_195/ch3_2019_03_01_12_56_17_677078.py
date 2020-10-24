import math
def calcula_gaussiana(x,μ,σ):
    y=1/(σ*((2*math.pi)**1/2))*(math.e**(-0.5*((x-μ)/σ)**2)
    return y
x=10
μ=50
σ=2
print(calcula_gaussiana(x,μ,σ))
