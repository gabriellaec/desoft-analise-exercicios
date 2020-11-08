from math import math.pi as pi
from math import math.exp 
from math import math.sqrt

def calcula_gaussiana(x,mi,sig):
    f = (1/sig*math.sqrt(2*pi))*(math.exp(-0.5*(((x-mi)/sig)**2))
    return f