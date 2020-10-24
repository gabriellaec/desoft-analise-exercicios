import math
def snell_descartes(n1,n2,o1):
    o1 = math.radians(o1)
    sen = n1*math.sin(o1)/n2
    o2_rad = math.asin(sen)
    o2 = math.degrees(o2_rad)
    return o2
    