def calcula_gaussiana(x, μ, σ):
    return(1/(σ*(2*π)**2)*e**(-0.5*((x-μ)/σ)**2))