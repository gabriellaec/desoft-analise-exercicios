import math
def snell_descartes(n1, n2, o1):
    o1=math.radient(o1)
    o2=n1*math.sin(o1)/n2
    math.degrees(o2)
    return o2