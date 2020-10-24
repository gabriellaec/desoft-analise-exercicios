import math
def reflexao_total_interna (a, b, d):
    y = (b * math.sin(math.radians(d))) / a
    z = math.asin(y)
    c = math.degrees (z)
    if c >= 90:
        return ('falso')
    else:
        return ('verdadeiro')