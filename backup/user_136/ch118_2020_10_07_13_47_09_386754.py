import math

def reflexao_total_interna(n1, n2, teta2):
    w= n2 * math.sin(math.radians(teta2)) / n1
    if w > 1:
        return True
    else:
        return False