import math

def snell_descartes(n1, n2, o1):
    o1 = math.radian(o1)
    o2 = math.asin(n1*math.sin(o1)/n2)
    o2 = math.degrees(o2)
    return o2