import math

def reflexao_total_interna (n1, n2, teta2):
    if n2>n1 and math.sin(math.radian(teta2)) == 0:
        return True
    else:
        return False
    