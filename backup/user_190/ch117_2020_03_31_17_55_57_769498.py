import math 
def snell_descartes(n1, n2, o1):
    x=((math.sin(math.degrees(o1)))*n1)/n2
    o2=math.sin(math.degrees(x))
    return (o2)