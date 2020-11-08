def calcula_gaussiana(x, u, s):
    Tt=(1/s*(2*3.14)**1/2)*2.7**(-1/2((x-u)/s)**2)
    return Tt
print (calcula_gaussiana(1, 2,  3)