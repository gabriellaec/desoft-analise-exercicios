import math
def snell_descartes(n1,n2,teta1):
    teta1r = math.radians(teta1)
    sen = math.sin(teta1r) * n1 / n2
    y = math.degrees(math.asin(sen))
    return y