import math

e=2.7182818284590452353602874713527

def calcula_gaussiana(x, μ, σ):
    y = (1 / (σ *((2*3.14)**2)))*(e**(-0.5*((x-μ)/σ)**2))
    return y