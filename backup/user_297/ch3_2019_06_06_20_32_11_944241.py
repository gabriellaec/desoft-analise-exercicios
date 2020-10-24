def calcula_gaussiana(x,y,z):
    a=z*((2*3.14)**0.5)
    b=(-0.5*(x-y/z)**2)
    f=a**b
    return f
print(calcula_gaussiana(10,2,3))