def calcula_gaussiana(x, μ, σ):
    f=(1/σ*2.506)*2.718**(-0.5*(((x-μ)/σ)**2))
    return f
