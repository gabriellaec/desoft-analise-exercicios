import math
# math.asin
def snell_descartes(n1,n2,O1,O2)
    O2= n1*math.sin(math.degrees(O1))/n2
    return O2