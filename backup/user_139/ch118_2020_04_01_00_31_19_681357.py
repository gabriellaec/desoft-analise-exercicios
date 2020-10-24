import math
def reflexao_total_interna (a, b, d):
    y = (b * math.sin(math.radians(d))) / a
    z = math.asin(y)
    return math.degrees (z)
if z == 90 or z > 90:
    print ('falso')
else:
    print ('verdadeiro')