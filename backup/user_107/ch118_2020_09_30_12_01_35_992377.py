import math

def reflexao_total_interna (n1, n2, tetta1):
    sin_tetta1 = math.sin(math.radians(tetta1))
    sin_tetta2 = n1 / n2 * sin_tetta1

    if sin_tetta2 > 0:
        return True
    else:
        return False
    