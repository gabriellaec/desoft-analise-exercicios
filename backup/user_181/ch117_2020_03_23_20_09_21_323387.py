def snell_descartes(n1,n2,a1):
    import math
    x = n2/math.sin(math.radians(a1))*n1
    y = math.sin(math.radians(x))
    z = math.degrees(y)
    return z