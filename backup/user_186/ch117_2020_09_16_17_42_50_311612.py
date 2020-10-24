import math
def snell_descartes (n1, n2, teta1) :
    y = math.arcsin(n1*math.sin(teta1)/n2)*(180/math.pi)
    return y 