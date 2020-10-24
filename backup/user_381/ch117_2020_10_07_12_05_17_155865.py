import math
def snell_descartes(n1, n2, o1):
    o2 = (n1*math.sin(math.radians(o1)))/n2
    o2 =  math.sin(math.radians(o2))
    return y