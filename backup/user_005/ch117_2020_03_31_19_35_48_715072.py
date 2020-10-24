import math
def snell_descartes (n1, n2, O1):
    O2 = (n1*math.sin(O1))/n2
    return O2