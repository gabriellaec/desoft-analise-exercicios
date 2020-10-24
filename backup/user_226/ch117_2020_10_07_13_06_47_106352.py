import math

def snell_descartes(n1, n2, O1):
    O1 = math.radians(O1)
    seno_de_O2 = n1 * math.sin(O1) / n2
    O2 = math.asin(seno_de_O2)
    O2 = math.degrees(O2)
    return O2