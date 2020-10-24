import math

def reflexao_total_interna (n1, n2, tetta2):
    if n1 < n2 and math.sin(math.radians(tetta2)) > 0:
        return False
    else:
        return True
