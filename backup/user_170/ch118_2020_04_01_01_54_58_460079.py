import math
def snell_descartes(n1, n2, a2):
    a2 = a2 * (math.pi/180)
    a1 = math.asin((math.sin(a2))*n2/n1)
    a1 = a1 * (180/math.pi)
    if a1 > 1:
        return True
    else:
        return False