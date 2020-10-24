import math
def snell_descartes(n1, n2, o1):
    y =  math.sin(math.radians(o2))
    y = (n1*math.sin(math.radians(o1)))/n2
    return y