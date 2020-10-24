import math
def snell_descartes(n1,n2,o1):
    o2=math.asin(n1*math.sin(o1))*math.pi/180
    return o2