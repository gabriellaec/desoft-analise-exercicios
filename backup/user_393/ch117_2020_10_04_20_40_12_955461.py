import math

def snell_descartes(n1,n2,teta1):
    y= math.radians(math.asin((n1/n2)*math.sin(math.radians(teta1))))
    return y
