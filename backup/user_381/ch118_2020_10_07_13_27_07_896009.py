import math
def reflexao_total_interna(n1, n2, teta2):
    o1 = (n2/n1)*math.sin(math.radians(teta2))
    seno1 = math.degrees(math.sin(math.radians(o1)))
    if seno1 > 1:
        return True
    elif seno1 <= 0:
        return False