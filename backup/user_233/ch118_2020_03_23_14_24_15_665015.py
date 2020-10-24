from math import asin, sin, radians, degrees

def reflexao_total_interna(n1, n2, t2):
    
    sen_t1 = n2 * sin(t2) / n1
    
    return sen_t1 > 1
    