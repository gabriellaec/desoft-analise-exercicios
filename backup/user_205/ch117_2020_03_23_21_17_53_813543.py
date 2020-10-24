from math import sin, pi
def snell_descartes (n,p,a):
    d = sin(a)*(180/pi)
    y = ((n*d)/p)*(pi/180)
    return y