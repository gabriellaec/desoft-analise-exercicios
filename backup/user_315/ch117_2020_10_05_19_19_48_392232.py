import math
def snell_descartes(n1,n2,teta1):
    a = math.degrees(teta1)
    teta2 = (n1/n2)*math.sin(a)
    b = math.sin(teta2)
    return math.degrees(b)
