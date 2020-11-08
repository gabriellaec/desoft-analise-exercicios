import math
def calcula_gaussiana (x, y, z):
    a = 1/(z*(2* math.pi)**(1/2))
    c = ((x - y)/z)**2
    b = (math.e) ** (-0.5*c)
    gaussiana = a*b
    return gaussiana