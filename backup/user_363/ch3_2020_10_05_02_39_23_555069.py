import math

e=2.718281828459045

def calcula_gaussiana(x, μ, σ):
    y = (1 / (σ *((2*3.14)**2)))*(e**(-0.5*((x-μ)/σ)**2))
    return y