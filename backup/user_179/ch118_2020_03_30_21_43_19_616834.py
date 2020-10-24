import math
def reflexao_total_interna (n1,n2,teta2):
    teta_radianos = math.radians(teta2)
    c = math.sin(teta_radianos) * n2
    if (n1 == c):
        return True
    else:
        return False