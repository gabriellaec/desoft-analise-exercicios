import math
def snell_descartes(n1,n2,o1):
    math.sin(math.radians(o2))=(math.sin(math.radians(o1))*n1)/n2
    return  math.sin(math.radians(o2))
    print(o1,o2)