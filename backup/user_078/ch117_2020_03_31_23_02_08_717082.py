import math
def snell_descartes (n1, n2, O1):
    O2= math.degrees(math.asin((n1*math.sin(math.radians(O1)))/n2))
    return O2