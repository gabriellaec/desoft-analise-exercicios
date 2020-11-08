def calcula_gaussiana(x, μ, σ):
    y = (1/(σ*((2*3.14)**(1/2))))*2.71**(-0.5*(((x-μ)/σ)**2))
    return y