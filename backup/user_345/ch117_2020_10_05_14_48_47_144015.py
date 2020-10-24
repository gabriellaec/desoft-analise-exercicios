import math
def snell_descartes(n1, n2, a1):
    seno1 = math.sin(math.radians(a1))
    seno2 = (n1/n2)*seno1
    a2=math.degrees(math.asin(seno2))
    return a2