import math
def reflexao_total_interna (n1,n2,teta2):
    teta2 = math.radians(teta2)
    c = math.sin(teta2) * n2
    if (n1 == c):
        return True
    else:
        return False