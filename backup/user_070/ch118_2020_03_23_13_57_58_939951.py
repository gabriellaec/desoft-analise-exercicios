import math
def reflexao_total_interna(n1,n2,a2):
    a1=math.degrees(math.asin((n2*math.sin(math.radians(a2)))/n1))
    R = math.degrees(2*math.pi)
    if a1 > R:
        return True
    else:
        return False