def calcula_gaussiana (x, μ, σ) :
    y = (1/σ*(2*π)**(1/2))*e**(-1/2*((x-μ)/σ)**2)
    return y
x = 10
π = 3.1415
e = 1.61
μ = 2
σ = 1
b = calcula_gaussiana (x, μ, σ)
print (b)