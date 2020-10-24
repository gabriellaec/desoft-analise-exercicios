import math
def reflexao_total_interna(n1, n2, teta1):
    x = (n2*math.sin(teta2))/n1
    y = math.sin(x)
    if y > teta2:
        return True
    else:
        return False
    