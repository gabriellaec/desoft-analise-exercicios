import math
def calcula_gaussiana(x,y,z):
    y = 1/(z * ((2*math.pi)**1/2)) * math.e **(-0.5 * (((x - y)/z)**2))
    return y
