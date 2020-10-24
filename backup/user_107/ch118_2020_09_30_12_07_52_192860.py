import math

def reflexao_total_interna (n1, n2, tetta2):
    if n1 > n2 and math.degrees(tetta2) < 90:
        return True
    else:
        return False
