from math import sin, pi, radians
def snell_descartes (n,p,a):
    d = sin(radians(a))
    y = sin(radians(((n*d)/p)))*(180/pi)
    return y