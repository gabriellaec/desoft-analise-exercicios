import math
def snell_descartes(n1,n2,o1):
    sen = n1*math.sin(o1)/n2
    o2 = math.arcsin(sen)
    return o2
    