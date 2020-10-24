from math import asin, sin, radians, degrees

def snell_descartes(n1, n2, t1):
    
    sin_t2 = n1 * sin(radians(t1)) / n2
    return degrees(asin(sin_t2))
    
def reflexao_total_interna(n1, n2, t2):
    
    try:
        snell_descartes(n2, n1, t2)
        return False
    
    except: return True
    