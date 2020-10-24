from math import sin, pi, radians
import numpy as np
def snell_descartes (n,p,a):
    d = sin(radians(a))*(180/pi)
    y = sin(radians(((n*d)/p)))*(180/pi)
    return y