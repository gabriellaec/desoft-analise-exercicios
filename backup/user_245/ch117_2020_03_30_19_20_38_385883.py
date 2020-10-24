import math
def snell_descartes(n1,n2,t1):
    t3 = math.degrees(math.asin(n1*(math.sin(math.radians(t1)))/n2))
    return t3