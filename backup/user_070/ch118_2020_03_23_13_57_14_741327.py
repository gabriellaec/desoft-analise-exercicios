import math
def reflexao_total_interna(n1,n2,a1):
    a2=math.degrees(math.asin((n1*math.sin(math.radians(a1)))/n2))
    R = math.degrees(2*math.pi)
    if a2 > R:
        return True
    else:
        return False