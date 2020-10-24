import math
def reflexao_total_interna(n1, n2, teta2):
    teta2 = math.radians(teta2)
    senoteta1 = n2*math.sin(teta2)/n1
    if senoteta1 > 1:
        return True
    else:
        return False