import math
def snell_descartes(n1, n2, o1):
    o2=math.asin((n1/n2)*(math.sin(math.radians(o1)))
    emd=math.degrees(o2)
    return emd

print(snell_descartes(1,2,30))                