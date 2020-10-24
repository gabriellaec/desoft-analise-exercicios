import math
def snell_descartes(n1,n2,o1):
    a = math.radians(o1)
    b = math.sin(a)
    c = n1/n2 * b
    d = math.asin(c)
    e = math.degrees(d)
    return e
    