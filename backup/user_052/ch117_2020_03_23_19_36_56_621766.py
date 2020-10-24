import math
def snell_descartes (n1,n2,o1):
    x = n1 * math.sin(o1)/n2
    x = math.sin(x)
    print (x)