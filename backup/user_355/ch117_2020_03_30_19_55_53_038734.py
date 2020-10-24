import math
def snell_descartes (o1, n1, n2 ):
    o2 =math.asin(math.sin(o1)*(n1/n2))
    y = o2 * 180 / math.pi
    return degrees ( math.arcsin ( o2 ))
