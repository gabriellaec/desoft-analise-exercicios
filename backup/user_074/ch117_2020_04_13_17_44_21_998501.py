import math
def snell_descartes(n1,n2,o2):
    a=n2/n1
    b=math.sin(math.degrees(o2))/math.sin(math.degrees(o1))
    a/b=0
    print(math.degrees(o1))
    return math.degrees(o1)