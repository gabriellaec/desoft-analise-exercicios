import math
def calcula_gaussiana(x,y,z):
    resultado = (1/(z*math.sqrt(2*math.pi)))*math.exp(-0.5*((x-y)/z)**2)
    return resultado