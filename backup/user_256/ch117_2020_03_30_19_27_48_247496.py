import math
def  snell_descartes(n1, n2, t1):
    t2= math.asin((n1/n2)*(math.radians(t1)))
    return math.degress(t2)
   