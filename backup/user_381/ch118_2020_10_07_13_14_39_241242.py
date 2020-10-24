import math
def reflexao_total_interna(n1, n2, o2):
    o1 = (n2/n1)*math.sin(math.radians(o2))
    seno1 = math.degrees(math.sin(o1))
    if o1 > 1:
        return True
    elif o1 <= 0:
        return False