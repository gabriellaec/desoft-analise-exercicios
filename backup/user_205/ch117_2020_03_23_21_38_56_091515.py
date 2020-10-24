from math import sin, pi, radians
from numpy import arcsin
def snell_descartes (n,p,a):
    d = sin(radians(a))*(180/pi)
    z = radians(((n*d)/p))
    y = arcsin(z)*(180/pi)
    return y