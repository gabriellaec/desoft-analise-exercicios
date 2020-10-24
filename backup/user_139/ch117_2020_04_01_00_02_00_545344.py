import math
def snell_descartes (a, b, c:
    y = (a * math.sin(math.radians(c))) / b
    z = math.asin(y)
    return math.degrees (z)