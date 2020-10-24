import math
def reflexao_total_interna (a, b, d):
    y = (b * math.sin(math.radians(d))) / a
    z = math.degrees(math.asin (y))
    if z >= 90:
        return False
    else:
        return True