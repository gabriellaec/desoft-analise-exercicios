from math import sin, pi, radians
def snell_descartes (n,p,a):
    d = sin(radians(a))*(180/pi)
    z = radians(((n*d)/p))
    y = sin(z)*(180/pi)
    return y