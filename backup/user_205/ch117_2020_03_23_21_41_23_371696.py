from math import sin, pi, radians
import numpy as np
def snell_descartes (n,p,a):
    d = sin(radians(a))*(180/pi)
    z = radians(((n*d)/p))
    y = np.arcsin(z) *(180/pi)
    return y