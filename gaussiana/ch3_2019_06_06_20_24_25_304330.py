def calcula_gaussiana(x,y,z):
    f=1/z((2*math.pi)**1/2)**(-0.5(x-y/z)**2)
    return f
print(calcula_gaussiana(10,2,3))