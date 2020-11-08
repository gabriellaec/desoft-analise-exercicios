def calcula_gaussiana(x,μ,σ):
    g = (1/(σ * ((2 * π) ** 0.5))) * (e ** (-0.5 * (((x - μ)/σ) ** 2)))
    π = 3.141592
    return g