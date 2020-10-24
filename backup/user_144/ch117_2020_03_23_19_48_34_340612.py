from math import sin, asin, radians

def snell_descartes(n1,n2,θ1):
    teta = sin(radians(θ1)) * n1 / n2
    teta2 = asin(teta)
    return teta2


