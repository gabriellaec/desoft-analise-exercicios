import math
def snell_descartes (o1, n1, n2 ):
    o2 =asin(math.sin(o1)*(n1/n2))
    y = o2 * 180 / math.pi
    return degrees ( arcsin ( o2 ))
