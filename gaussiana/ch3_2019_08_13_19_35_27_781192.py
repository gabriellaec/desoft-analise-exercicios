import math
def calcula_gaussiana(w,x,z):
    y=1/(z(2*math.pi)**(1/2))*math.exp(-0.5*(w-x)**2/z)
    return y