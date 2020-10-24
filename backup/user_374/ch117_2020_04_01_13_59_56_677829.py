import math

def snell_descartes(n1,n2,teta1):
    teta = (n1 * math.sin(math.radians(teta1)))/n2
    teta2 = math.asin(teta)
    return math.degrees(teta2)
