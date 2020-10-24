import math
def reflexao_total_interna (a, b, d):
    y = (b * math.sin(math.radians(d))) / a
    if y > 1:
        return True
    else:
        return False