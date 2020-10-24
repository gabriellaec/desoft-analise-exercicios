import math
def snell_descartes(n1, n2, a1):
    a1 = a1 * (math.pi/180)
    a2 = math.asin((n1*math.sin(a1))/n2)
    a2 = a2 * (180/math.pi)
    return a2
    