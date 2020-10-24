import math

def reflexao_total_interna(n1, n2, teta2):
    teta2_rad = math.radians(teta2)
    senoTeta1_rad = (n2/n1) * math.sin(teta2_rad)
    if senoTeta1_rad > 1:
        return True
    return False 
