from math import sqrt
from math import pi
def calcula_gaussiana(x,y,z):
    y= (1/(z*sqrt*(2*pi)))**(-(0.5)*((x-y)/z)**2)
    return y 
    
