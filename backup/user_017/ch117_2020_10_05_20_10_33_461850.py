import math
def snell_descartes(n1,n2,x):
    y= math.asin((math.sin(x)*n1)/n2)
    return y
