import math
def snell_descartes(n1, n2, teta1):
    teta2 = math.arcsin((n1*math.sin(teta1))/n2)
    return teta2