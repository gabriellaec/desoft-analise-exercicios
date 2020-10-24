import math
def snell_descartes(n1,n2,a1):
    A = ((math.pi/180)*math.sin(n1))
    B = ((math.pi/180)*math.sin(n2))
    a2 = a1 * A/B
    return a2
