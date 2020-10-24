import math
def snell_descartes(n1,n2,O1):
    a = math.radians(O1)
    b = math.sin(a)
    c = math.degrees(b)
    d = n1/n2*c
    return d