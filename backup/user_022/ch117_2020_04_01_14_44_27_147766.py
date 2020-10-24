import math
def snell_descartes(n1, n2, o1):
    o1rad = o1*math.pi/180
    o2 = math.asin(math.sin(o1rad)*(n1/n2)
    y = o2 * 180 / math.pi
    return y
    
    
