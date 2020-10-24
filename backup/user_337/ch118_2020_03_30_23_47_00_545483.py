import math
def reflexao_total_interna(n1, n2, x):
    y = math.asin(math.sin(math.radians(x)) * (n1/n2))
    z=math.degrees(y)
    if z == 90:
        return True
    else:
        return False



