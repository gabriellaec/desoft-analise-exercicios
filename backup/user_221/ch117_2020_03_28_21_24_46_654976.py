import math
def snell_descartes(n1, n2, teta1):
    teta2 = math.asin((n1*math.sin(math.radian(teta1)))/n2)
    return teta2