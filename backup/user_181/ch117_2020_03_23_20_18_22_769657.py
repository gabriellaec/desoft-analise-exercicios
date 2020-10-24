def snell_descartes(n1,n2,a1):
    import math
    x = n1/n2 * math.sin(math.radians(a1))
    y = math.asin(x)
    a2 = math.degrees(y)
    return a2