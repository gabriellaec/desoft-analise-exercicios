def snell_descartes (n1, n2, o1):
    import math
    x = n1 * math.sin(math.radians(o1))/n2
    y = math.asin(x)
    o2 = math.degrees(y)
    return o2
    