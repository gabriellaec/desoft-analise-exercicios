import math
def snell_descartes(n1, n2, o1):
    seno2 = (n1*math.sin(o1))/n2
    o2 =  math.degrees(math.asin(seno2))
    return o2