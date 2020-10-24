def calcula_gaussiana(x,m,s):
    import math
    g=(1/(s*(1/(2*math.pi))))*math.exp((-0,5*((x-m)/s)**2))
    return g