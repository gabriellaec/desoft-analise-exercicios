import math
def snell_descartes (n1, n2, o1):
    x = (n1*math.sin(math.radians(o1)))/n2
    o2 = math.asin(x)
    return math.deegres(o2)