from math import sin, pi
def snell_descartes (n,p,a):
    af = sin(a)*(180/pi)
    y = ((n*a)/p)*pi/180
    return y