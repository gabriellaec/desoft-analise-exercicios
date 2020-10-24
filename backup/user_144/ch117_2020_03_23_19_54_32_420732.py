from math import sin, asin, radians, degrees

def snell_descartes(n1,n2,θ1):
    teta = sin(radians(θ1)) * n1 / n2
    teta2 = degrees(asin(teta))
    return teta2


