import math
def snell_descartes(n1,n2,o):
    o2 = math.asin((n1 * math.sin(math.radians(o)))/ n2)
    graus = math.degrees(o2)
    return graus

def reflexao_total_interna(n1,n2,o2):
    o = math.asin((n1 * math.sin(math.radians(o2)))/ n2)
    if o >= 90:
        return True
    else:
        return False
    
    