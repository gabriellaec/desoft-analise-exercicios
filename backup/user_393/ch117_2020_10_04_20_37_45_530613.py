import math

def snell_descartes(n1,n2,teta1):
    y= math.degrees(math.asin((n2/n1)*math.sin(teta1)))
    return y
