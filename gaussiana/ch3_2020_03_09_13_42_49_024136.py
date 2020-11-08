import math
def calcula_gaussiana(x,u,a):
    b=1/a*(2*math.pi)**(1/2)
    c= (-0.5*((x-u)/a)**2)
    fo= b*math.e**c
    return fo

x=4
u=3
a=2
calculo= calcula_gaussiana(x,u,a)
print (calculo)
