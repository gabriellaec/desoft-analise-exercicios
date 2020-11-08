impot.math
def calcula_gaussiana (x,y,z):
    f= (1/(z*(sqrt(2*pi)))*exp(-0.5*((x-y)/z)**2))
    return f