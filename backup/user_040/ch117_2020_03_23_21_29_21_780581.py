import math
def snell_descartes(n1,n2,teta1):
    return math.asin(math.degrees(n1*math.sin(math.degrees(teta1))/n2))