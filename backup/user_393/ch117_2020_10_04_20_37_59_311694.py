import math

def snell_descartes(n1,n2,teta1):
    y= math.degrees(math.asin((n1/n2)*math.sin(teta1)))
    return y
