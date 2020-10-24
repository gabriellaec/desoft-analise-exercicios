import math
def snell_descartes(n1,n2,o1):
    seno2=(n1/n2)*math.sin(math.radians(o1))
    o2=math.degrees(math.asin(seno2))
    return o2