import math

def snell_descartes(n1, n2, a1):
    a1 = math.radians(a1)
    a2 = (n1*math.sin(a1))/n2
    x = math.asin(a2)
    return x