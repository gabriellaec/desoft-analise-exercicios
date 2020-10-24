from math import sin, pi, radians, degrees, asin
def snell_descartes (n,p,a):
    x = (n*sin(radians(a)))/p
    y = asin(x)
    grau = degrees(y)
    return grau