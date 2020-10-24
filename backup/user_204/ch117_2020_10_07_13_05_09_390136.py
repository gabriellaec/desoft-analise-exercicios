import math
def snell_descartes(n1,n2,teta1):
    eq = n1 / n2
    eq2 = eq * math.sin(math.radians(teta1))
    return math.degrees(math.asin(eq2))