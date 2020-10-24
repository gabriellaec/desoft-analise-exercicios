import math

def snell_descartes (n1, n2, tetta1):
    sin_tetta1 = math.sin(math.radians(tetta1))
    sin_tetta2 = n1 / n2 * sin_tetta1
    
    return math.degrees(math.asin(sin_tetta2))

def reflexao_total_interna (n1, n2, tetta2):
    tetta1 = snell_descartes(n2, n1, tetta2)
    sin_tetta1 = math.sin(tetta1)
    
    if and sin_tetta1 > 1:
        return True
    else:
        return False
