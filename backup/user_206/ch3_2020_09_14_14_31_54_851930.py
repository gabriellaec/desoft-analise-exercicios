import math

def calcula_gaussiana(x, y, z):
    f = 1/(z * math.sqrt(2* math.pi)) * math.e ** ((-0.5*((x- y) / z)) ** 2)
    return(f)