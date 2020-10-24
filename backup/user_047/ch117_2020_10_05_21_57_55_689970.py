import math
def snell_descartes(n1,n2,o1):
    x = math.radians(o1)
    conta = (n1/n2)*math.sin(x)
    s = math.asin(conta)
    z = math.degrees(s)
    return z