import math
def snell_descartes(n1,n2,o1):
    o1=math.radians(o1)
    o2=math.sin((math.sin(o1)*n1/n2))
    o2=math.degrees(o2)
    return o2
    
