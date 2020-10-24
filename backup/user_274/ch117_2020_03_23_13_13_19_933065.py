def snell_descartes(n1, n2, t1):
    import math
    t1 = math.radians(t1)
    t2 = math.asin(math.sin(t1)*n1/n2)
    t2 = math.degrees(t2)
    return t2