from math import radians
from math import sin
from math import degrees
from math import asin
def reflexao_total_interna(n1,n2,a2):
    x = sin(radians(a2))*n2/n1
    y = asin(x)
    a = degrees(y)
    if a > 1:
        return True
    else:
        return False