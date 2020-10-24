import math
def snell_descartes(n1, n2, x):
    y = math.asin(math.sin(math.radians(x)) * (n1/n2))
    z=math.degrees(y)
    return z
