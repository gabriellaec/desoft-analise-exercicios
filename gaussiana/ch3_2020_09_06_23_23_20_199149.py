def calcula_gaussiana(x, y, z):
    w= 1/(z*(2*pi)**(1/2))*e**(-0.5*(x-y/z)**2)
    return w

a= 20
b=10
c=5
d= calcula_gaussiana(a, b, c)
print('gaussiana é {0}'. format(d)) 