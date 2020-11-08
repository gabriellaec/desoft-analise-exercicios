import math
def calcula_gaussiana (x,y,z):
    f=1/(z*((2*math.pi)**(1/2))
    g=math.e**(-0.5*((x-y)/z)**2)
    h=g*f
    return h