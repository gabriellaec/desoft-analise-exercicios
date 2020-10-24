import math
def reflexao_total_interna(n1, n2, teta2):
    teta2 = math.radians(teta2)
    a = (n2* math.sin(teta2)) / n1
    if a > 1:
        return True
    else:
        return False
    