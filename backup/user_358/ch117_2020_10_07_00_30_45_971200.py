import math
def snell_descartes (n1,n2,o1):
    a=n1*(math.sin(math.radians(o1)))
    o2=a/n2
    return math.sin(math.radians(o2))
