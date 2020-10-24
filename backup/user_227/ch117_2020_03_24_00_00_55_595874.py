import math

def snell_descartes(n1, n2, T1):
    
    T2 = math.degrees(math.asin(((n1 * (math.sin(math.radians(T1))))/n2)))
    
    return T2