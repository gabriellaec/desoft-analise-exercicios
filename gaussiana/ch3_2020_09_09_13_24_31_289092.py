import math
def calcula_gaussiana(x,y,z):
    g = 1/(z * ((2*math.pi)**0.5)) * (math.e **(-0.5 * (((x - y)/z)**2)))
    return g
