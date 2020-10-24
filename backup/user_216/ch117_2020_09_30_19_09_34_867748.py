import math
def snell_descartes(n1,n2,O1):
    O1 = math.radians(O1)
    O2 = math.asin(n1 * math.sin(O1)/n2)
    O2 = math.degrees(O2)
    return O2