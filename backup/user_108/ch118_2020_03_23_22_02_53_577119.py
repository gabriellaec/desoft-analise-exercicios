import math
def snell_descartes(n1,n2,a1):
    return math.degrees(math.asin(n1 * math.sin(math.radians(a1)) / n2))

def reflexao_total_interna(n1,n2,a1):
    return math.sin(math.radianssnell_descartes(n2,n1,a2)) > 1
