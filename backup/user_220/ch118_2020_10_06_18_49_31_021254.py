import math

def reflexao_total_interna(n1,n2,o2):
    o = math.asin((n1 * math.sin(math.radians(o2)))/ n2)
    graus = math.degrees(o)
    if graus > 90:
        return True
    else:
        return False
    
    