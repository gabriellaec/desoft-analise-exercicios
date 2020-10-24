import math
def snell_descartes (n1, n2, teta1):
    w = math.degrees(teta1)
    x =  (math.sin(w)*n1)/n2
    y = math.degrees(x)
    z = math.sin(y)
    return z
