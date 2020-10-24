import math
def snell_descartes(n1,n2,O1):
    O = math.radians(O1)
    a = math.sin(O)
    c = (n1/n2)*a
    O2 = math.degrees(c)
    return O2