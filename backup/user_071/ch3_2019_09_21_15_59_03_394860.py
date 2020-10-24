import math
def calcula_gaussiana(x, μ, σ):
    a=(2*math.pi)**(1/2)
    b=1/(σ*a)
    c=-0.5*(((x-μ)/σ)**2)
    d=math.e**c
    f= b*d
    return f