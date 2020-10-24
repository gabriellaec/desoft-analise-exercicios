from math import sin, pi, radians
def snell_descartes (n,p,a):
    d = sin(radians(a))*(180/pi)
    y = radians(((n*d)/p))*(pi/180)
    return y