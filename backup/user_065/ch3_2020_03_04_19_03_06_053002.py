import math 
def calcula_gaussiana(x,y,z):
    resultPt1 = (1/(z*math.sqrt(2*math.pi)))
    resultPt2 = math.e**(-0.5*(x-y/z)**2)
    resultFinal = resultPt1 * resultPt2
    return resultFinal