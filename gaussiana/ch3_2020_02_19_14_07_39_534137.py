def calcula_gaussiana(x, μ, σ):
    return(1/(σ*((2*π)**0.5))*e**(-0.5*((x-μ)/σ)**2))