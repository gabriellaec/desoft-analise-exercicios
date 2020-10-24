import math

def snell_descartes (n1, n2, tetta1):
    sin_tetta1 = math.sin(math.radians(tetta1))
    sin_tetta2 = n1 / n2 * sin_tetta1
    
    return math.degrees(math.asin(sin_tetta2))
