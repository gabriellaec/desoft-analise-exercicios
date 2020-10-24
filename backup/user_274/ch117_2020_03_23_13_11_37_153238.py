def snell_descartes(n1, n2, t1):
    import math
    t1 = radians(t1)
    t2 = sin**-1(sin(t1)*n1/n2)
    t2 = degrees(t2)
    return t2