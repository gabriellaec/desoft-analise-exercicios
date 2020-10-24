def calcula_gaussiana(x, y, z):
    w= 1/(z*(2*π)**(1/2))*e**(-0.5*(x-y/z)**2)
    return w

