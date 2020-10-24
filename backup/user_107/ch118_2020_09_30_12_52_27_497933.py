import math

def snell_descartes (n1, n2, tetta1):
    
    return math.degrees(math.asin(sin_tetta2))

def reflexao_total_interna (n1, n2, tetta2):
    sin_tetta2 = math.sin(math.radians(tetta2))
    sin_tetta1 = n1 / n2 * sin_tetta2
    
    if sin_tetta1 > 1:
        return True
    else:
        return False
