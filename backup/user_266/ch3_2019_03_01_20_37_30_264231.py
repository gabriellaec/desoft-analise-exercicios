import math
import numpy as np
def calcula_gaussiana(x,y,o):
    gauss = 1/(o*(2*math.pi)**(1/2))*np.exp(-0.5((x-y)/o)**2)
    return gauss