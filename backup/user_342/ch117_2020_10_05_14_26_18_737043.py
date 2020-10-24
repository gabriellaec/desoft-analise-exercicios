import math
def snell_descartes(n1,n2,o1):
    o1=math.radians(o1)
    sen_o2=math.sin(o1)*(n1/n2)
    o2=math.asin(sen_o2)
    o2=math.degrees(o2)
    return o2
    