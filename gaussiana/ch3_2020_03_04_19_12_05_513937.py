import math 
def calcula_gaussiana(x,y,z):
    if x or y is 0:
        return
    if x or y or z is math.sqrt(2*math.pi):
        return

    resultPt1 = (1/(z*math.sqrt(2*math.pi)))
    resultPt2 = math.e**(-0.5*(x-y/z)**2)
    resultFinal = resultPt1 * resultPt2
    return resultFinal