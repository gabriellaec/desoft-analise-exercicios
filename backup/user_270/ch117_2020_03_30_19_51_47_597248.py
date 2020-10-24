import math
def snell_descartes(n1,n2,o1):
    sen = n1*math.sin(o1)/n2
    o2_rad = math.asin(sen)
    o2 = 180*o2_rad/(2*math.pi)
    return o2
    