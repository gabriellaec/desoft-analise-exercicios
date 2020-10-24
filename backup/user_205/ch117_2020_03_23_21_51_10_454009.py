from math import sin, pi, radians
def snell_descartes (n,p,a):
    d = sin(radians(a))*(180/pi)
    y = radians(((n*d)/p))*(180/pi)
    inverso = 1/y
    return inverso