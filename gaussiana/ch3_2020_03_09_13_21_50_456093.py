def calcula_gaussiana(x, μ, σ):
    f=(1/σ*2.506)*2.718**(-0.5*(((x-μ)/σ)**2))
    return f

print(calcula_gaussiana(0, 0, 1))
print(calcula_gaussiana(0, 0.3989, 0.3989))
print(calcula_gaussiana(1, 1, 1))
print(calcula_gaussiana(10000, -10000, 0.1))