from math import sin, asin, radians

def snell_descartes(n1,n2,θ1):
    teta = radians((sin(θ1)) * n1) / n2
    teta2 = radians(asin(teta))
    return teta2


