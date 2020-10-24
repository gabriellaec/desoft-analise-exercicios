import math
def snell_descartes(n1,n2,o2):
    a=n2/n1
    b=math.sin(math.degree(o2))/math.sin(math.degree(o1))
    if a=b:
        return math.degree(o1)