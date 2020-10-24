import math
def snell_descartes (n1,n2,o1):
    o2= (n1/n2)*math.sin(math.degrees(o1))

    return o2