import math

def snell_descartes (n1, n2 , tetta1):
    tetta2 = math.asin(n1*math.sin(math.radians(tetta1))/n2)
    return